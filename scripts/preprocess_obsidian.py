#!/usr/bin/env python3
"""
Obsidian to Quartz Preprocessor

This script transforms Obsidian-specific syntax to be compatible with Quartz.
It is IDEMPOTENT - safe to run multiple times without breaking already processed files.

Transformations:
1. Rename files with spaces → dashes
2. Convert markdown image links → WikiLinks: ![](attachments/file.png) → ![[file.png]]
3. Fix nested heading links: [[#Parent#Child|Text]] → [[#Child|Text]]
4. Convert tab indentation → spaces in lists
5. Replace non-breaking spaces → regular spaces
6. Update all WikiLinks to use dashed filenames
7. Fix broken asset links → move assets to correct section's attachments folder

Usage:
    python preprocess_obsidian.py [content_dir]
    
    content_dir: Path to the Quartz content directory (default: ./content)
"""

import os
import re
import shutil
import sys
from pathlib import Path


def rename_files_with_spaces(content_dir: Path) -> dict[str, str]:
    """
    Rename all files and directories with spaces to use dashes.
    Returns a mapping of old names to new names for link updates.
    
    This is idempotent - files already using dashes are skipped.
    """
    renames = {}
    
    # Process from deepest to shallowest to avoid path issues
    all_paths = sorted(content_dir.rglob("*"), key=lambda p: len(p.parts), reverse=True)
    
    for path in all_paths:
        if " " in path.name:
            new_name = path.name.replace(" ", "-")
            new_path = path.parent / new_name
            
            if not new_path.exists():
                path.rename(new_path)
                # Store relative paths for link updates
                rel_old = path.relative_to(content_dir)
                rel_new = new_path.relative_to(content_dir)
                renames[str(rel_old)] = str(rel_new)
                print(f"  Renamed: {rel_old} → {rel_new}")
    
    return renames


def transform_image_links(content: str) -> str:
    """
    Convert markdown image syntax to WikiLink syntax.
    
    Transforms:
        ![](attachments/file.png) → ![[file.png]]
        ![alt](attachments/file.png) → ![[file.png]]
        ![](./attachments/file.png) → ![[file.png]]
    
    Idempotent: Already converted WikiLinks are not affected.
    """
    # Pattern for markdown images with attachments path
    # Matches: ![optional-alt](attachments/filename) or ![](./attachments/filename)
    pattern = r'!\[[^\]]*\]\(\.?/?attachments/([^)]+)\)'
    
    def replace_match(match):
        filename = match.group(1)
        # URL decode if needed (e.g., %20 → space, then to dash)
        filename = filename.replace("%20", "-")
        return f"![[{filename}]]"
    
    return re.sub(pattern, replace_match, content)


def transform_nested_heading_links(content: str) -> str:
    """
    Convert nested Obsidian heading links to simple heading links.
    
    Transforms:
        [[#Parent#Child|Display]] → [[#Child|Display]]
        [[#Parent#Child]] → [[#Child]]
    
    Idempotent: Simple heading links are not affected.
    """
    # Pattern for nested heading WikiLinks with optional display text
    # Matches: [[#Something#Something|optional text]]
    pattern = r'\[\[#[^#\]]+#([^\]|]+)(\|[^\]]+)?\]\]'
    
    def replace_match(match):
        heading = match.group(1)
        display = match.group(2) if match.group(2) else f"|{heading}"
        return f"[[#{heading}{display}]]"
    
    return re.sub(pattern, replace_match, content)


def transform_tab_indentation(content: str) -> str:
    """
    Convert tab indentation to spaces in list items.
    
    Transforms:
        <tab><tab>- item → 4 spaces + - item
    
    Idempotent: Already space-indented lists are not affected.
    """
    # Replace tabs at start of lines followed by list markers
    lines = content.split('\n')
    result = []
    
    for line in lines:
        # Count leading tabs
        tab_count = 0
        for char in line:
            if char == '\t':
                tab_count += 1
            else:
                break
        
        if tab_count > 0:
            # Replace tabs with 2 spaces each (standard markdown)
            spaces = "  " * tab_count
            line = spaces + line[tab_count:]
        
        result.append(line)
    
    return '\n'.join(result)


def transform_non_breaking_spaces(content: str) -> str:
    """
    Convert non-breaking spaces (\xa0) to regular spaces.
    
    Idempotent: Already regular spaces are not affected.
    """
    return content.replace('\xa0', ' ')


def transform_all_wikilinks(content: str) -> str:
    """
    Update ALL WikiLinks to use dashed filenames.
    Transforms:
        [[Note Name]] → [[Note-Name]]
        ![[Image Name.png]] → ![[Image-Name.png]]
        [[Note Name|Alias]] → [[Note-Name|Alias]]
    
    Idempotent: Links already using dashes are not affected.
    """
    # Pattern matches [[Target]] or [[Target|Alias]]
    # Group 1: Optional ! (for images)
    # Group 2: Target filename (before | or ])
    # Group 3: Optional alias (from | to ])
    pattern = r'(!?)\[\[([^\]|]+)(\|[^\]]+)?\]\]'
    
    def replace_match(match):
        is_image = match.group(1)
        target = match.group(2)
        alias = match.group(3) if match.group(3) else ""
        
        # Only replace spaces in the target filename
        if " " in target:
            new_target = target.replace(" ", "-")
            return f"{is_image}[[{new_target}{alias}]]"
        
        return match.group(0)
    
    return re.sub(pattern, replace_match, content)


def update_internal_links(content: str, renames: dict[str, str]) -> str:
    """
    Update WikiLinks to use new (dashed) filenames.
    
    Idempotent: Links already using dashed names are not affected.
    """
    for old_path, new_path in renames.items():
        old_name = Path(old_path).stem
        new_name = Path(new_path).stem
        
        # Update [[Old Name]] → [[New-Name]]
        content = content.replace(f"[[{old_name}]]", f"[[{new_name}]]")
        content = content.replace(f"[[{old_name}|", f"[[{new_name}|")
    
    return content


def find_and_fix_broken_assets(content_dir: Path) -> tuple[int, int]:
    """
    Find broken asset links in markdown files and attempt to fix them.
    
    For each markdown file:
    1. Find all WikiLink image references: ![[filename.ext]]
    2. Check if the asset exists in the section's attachments folder
    3. If not found locally, search all other attachment folders
    4. If found elsewhere, move it to the correct attachments folder
    5. If not found anywhere, print the missing asset and page name
    
    Returns: (fixed_count, missing_count)
    """
    # Build index of all attachment folders and their contents
    attachment_dirs = list(content_dir.rglob("attachments"))
    asset_index: dict[str, Path] = {}  # filename -> full path
    
    for attach_dir in attachment_dirs:
        if attach_dir.is_dir():
            for asset_file in attach_dir.iterdir():
                if asset_file.is_file():
                    # Store with lowercase key for case-insensitive matching
                    asset_index[asset_file.name.lower()] = asset_file
    
    fixed_count = 0
    missing_assets: list[tuple[str, str]] = []  # (asset_name, page_path)
    
    # Process all markdown files
    md_files = list(content_dir.rglob("*.md"))
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        
        # Find all WikiLink image references: ![[filename.ext]]
        pattern = r'!\[\[([^\]]+)\]\]'
        matches = re.findall(pattern, content)
        
        if not matches:
            continue
        
        # Determine the expected attachments folder for this file
        section_dir = md_file.parent
        expected_attach_dir = section_dir / "attachments"
        
        for asset_name in matches:
            # Normalize the asset name (replace spaces with dashes as per transform)
            normalized_name = asset_name.replace(" ", "-")
            expected_asset_path = expected_attach_dir / normalized_name
            
            # Check if asset exists in the expected location
            if expected_asset_path.exists():
                continue
            
            # Also check without normalization
            if (expected_attach_dir / asset_name).exists():
                continue
            
            # Asset not found locally - search in the global index
            lookup_key = normalized_name.lower()
            alt_lookup_key = asset_name.lower()
            
            found_path = asset_index.get(lookup_key) or asset_index.get(alt_lookup_key)
            
            if found_path and found_path.exists():
                # Found the asset elsewhere - move it to the correct location
                expected_attach_dir.mkdir(parents=True, exist_ok=True)
                dest_path = expected_attach_dir / found_path.name
                
                if not dest_path.exists():
                    shutil.move(str(found_path), str(dest_path))
                    print(f"  ✅ Moved: {found_path.name}")
                    print(f"     From: {found_path.parent.relative_to(content_dir)}")
                    print(f"     To:   {expected_attach_dir.relative_to(content_dir)}")
                    
                    # Update the index
                    del asset_index[found_path.name.lower()]
                    asset_index[dest_path.name.lower()] = dest_path
                    fixed_count += 1
                else:
                    # Asset already exists at destination (duplicate?)
                    pass
            else:
                # Asset not found anywhere
                rel_page = md_file.relative_to(content_dir)
                missing_assets.append((asset_name, str(rel_page)))
    
    # Print missing assets
    if missing_assets:
        print()
        print("  ⚠️  Missing assets (not found anywhere):")
        for asset_name, page_path in missing_assets:
            print(f"     Asset: {asset_name}")
            print(f"     Page:  {page_path}")
            print()
    
    return fixed_count, len(missing_assets)


def process_markdown_file(file_path: Path, renames: dict[str, str]) -> bool:
    """
    Apply all transformations to a single markdown file.
    Returns True if file was modified, False otherwise.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        print(f"  Warning: Could not read {file_path} (encoding issue)")
        return False
    
    original = content
    
    # Apply transformations in order
    content = transform_non_breaking_spaces(content)
    content = transform_image_links(content)
    content = transform_all_wikilinks(content) # Sanitize generic WikiLinks
    content = transform_nested_heading_links(content)
    content = transform_tab_indentation(content)
    content = update_internal_links(content, renames)
    
    # Only write if changed
    if content != original:
        file_path.write_text(content, encoding='utf-8')
        return True
    
    return False


def main(content_dir: str = "./content"):
    """Main entry point."""
    content_path = Path(content_dir)
    
    if not content_path.exists():
        print(f"Error: Content directory '{content_dir}' does not exist")
        sys.exit(1)
    
    print(f"🔄 Preprocessing Obsidian notes in: {content_path.absolute()}")
    print()
    
    # Step 1: Rename files with spaces
    print("📁 Step 1: Renaming files with spaces...")
    renames = rename_files_with_spaces(content_path)
    print(f"   Renamed {len(renames)} files/directories")
    print()
    
    # Step 2: Process markdown files
    print("📝 Step 2: Transforming markdown content...")
    md_files = list(content_path.rglob("*.md"))
    modified_count = 0
    
    for md_file in md_files:
        if process_markdown_file(md_file, renames):
            modified_count += 1
            print(f"  Modified: {md_file.relative_to(content_path)}")
    
    print(f"   Modified {modified_count} of {len(md_files)} files")
    print()
    
    # Step 3: Find and fix broken asset links
    print("🔗 Step 3: Finding and fixing broken asset links...")
    fixed_count, missing_count = find_and_fix_broken_assets(content_path)
    print(f"   Fixed {fixed_count} broken asset links")
    if missing_count > 0:
        print(f"   ⚠️  {missing_count} assets could not be found")
    print()
    
    print("✅ Preprocessing complete!")
    print()
    print("Transformations applied:")
    print("  • File/folder names: spaces → dashes")
    print("  • Image links: ![](attachments/...) → ![[...]]")
    print("  • Heading links: [[#Parent#Child]] → [[#Child]]")
    print("  • List indentation: tabs → spaces")
    print("  • WikiLinks: [[With Spaces]] → [[With-Dashes]]")
    print("  • Non-breaking spaces: \\xa0 → space")
    print("  • Broken asset links: moved to correct section")


if __name__ == "__main__":
    content_dir = sys.argv[1] if len(sys.argv) > 1 else "./content"
    main(content_dir)
