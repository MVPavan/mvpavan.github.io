#!/usr/bin/env python3
"""
Sync Obsidian notes to Jekyll _notes collection.

This script reads publish_config.yaml and copies selected notes from the
Obsidian vault to the Jekyll _notes directory, transforming links and
ensuring proper frontmatter.
"""

import re
import shutil
from pathlib import Path
from typing import Any

import yaml


def load_config(config_path: Path) -> dict[str, Any]:
    """Load the publish configuration."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def should_include(file_path: Path, vault_path: Path, include_patterns: list[str], exclude_patterns: list[str]) -> bool:
    """Check if a file should be included based on patterns."""
    from fnmatch import fnmatch
    
    relative_path = file_path.relative_to(vault_path)
    rel_str = str(relative_path)
    
    # Check excludes first (they take precedence)
    for pattern in exclude_patterns:
        if fnmatch(rel_str, pattern):
            return False
        # Also check each part of the path for directory patterns
        for part in relative_path.parts:
            if fnmatch(part, pattern.replace("**", "*").replace("/", "")):
                if "**" in pattern:
                    return False
    
    # Check includes
    for pattern in include_patterns:
        if fnmatch(rel_str, pattern):
            return True
        if pattern == "**/*.md" and file_path.suffix == ".md":
            return True
    
    return False


def transform_wikilinks(content: str, all_notes: dict[str, str]) -> str:
    """
    Transform Obsidian [[WikiLinks]] to Jekyll markdown links.
    
    Args:
        content: The markdown content
        all_notes: Dict mapping note names to their URL paths
    """
    # Pattern for [[Link]] and [[Link|Display Text]]
    wikilink_pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
    
    def replace_link(match: re.Match) -> str:
        link_target = match.group(1).strip()
        display_text = match.group(2)
        
        if display_text is None:
            display_text = link_target
        
        # Convert to URL-friendly slug
        slug = link_target.lower().replace(" ", "-").replace("_", "-")
        
        # Check if it's in our known notes
        if link_target in all_notes:
            url = all_notes[link_target]
        else:
            url = f"/notes/{slug}/"
        
        return f"[{display_text}]({url})"
    
    return re.sub(wikilink_pattern, replace_link, content)


def transform_image_links(content: str, source_file: Path, vault_path: Path, assets_dir: Path) -> str:
    """
    Transform Obsidian image links to Jekyll asset paths and copy images.
    
    Handles:
    - ![[image.png]]
    - ![alt](path/to/image.png)
    """
    # Pattern for ![[image]]
    obsidian_img_pattern = r'!\[\[([^\]]+)\]\]'
    
    def replace_obsidian_img(match: re.Match) -> str:
        img_name = match.group(1).strip()
        # Search for the image in the vault
        for img_path in vault_path.rglob(img_name):
            if img_path.is_file():
                dest_path = assets_dir / img_path.name
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(img_path, dest_path)
                return f"![{img_path.stem}](/assets/images/{img_path.name})"
        return match.group(0)  # Keep original if not found
    
    content = re.sub(obsidian_img_pattern, replace_obsidian_img, content)
    
    # Also handle relative markdown image links
    md_img_pattern = r'!\[([^\]]*)\]\((?!http)([^)]+)\)'
    
    def replace_md_img(match: re.Match) -> str:
        alt_text = match.group(1)
        img_path_str = match.group(2)
        
        # Resolve relative path
        img_path = (source_file.parent / img_path_str).resolve()
        if img_path.exists():
            dest_path = assets_dir / img_path.name
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(img_path, dest_path)
            return f"![{alt_text}](/assets/images/{img_path.name})"
        return match.group(0)
    
    content = re.sub(md_img_pattern, replace_md_img, content)
    
    return content


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """Parse YAML frontmatter from markdown content."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].lstrip("\n")
                return frontmatter, body
            except yaml.YAMLError:
                pass
    return {}, content


def generate_frontmatter(frontmatter: dict[str, Any], defaults: dict[str, Any], title: str) -> str:
    """Generate YAML frontmatter string."""
    # Start with defaults, then override with existing frontmatter
    merged = {**defaults, **frontmatter}
    
    # Ensure title is set
    if "title" not in merged:
        merged["title"] = title
    
    lines = ["---"]
    for key, value in merged.items():
        if isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")
        elif isinstance(value, str) and (":" in value or "\n" in value):
            lines.append(f'{key}: "{value}"')
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    lines.append("")
    
    return "\n".join(lines)


def process_note(
    source_path: Path,
    dest_path: Path,
    vault_path: Path,
    assets_dir: Path,
    defaults: dict[str, Any],
    all_notes: dict[str, str],
) -> None:
    """Process a single note file."""
    content = source_path.read_text(encoding="utf-8")
    
    # Parse existing frontmatter
    frontmatter, body = parse_frontmatter(content)
    
    # Transform links
    body = transform_wikilinks(body, all_notes)
    body = transform_image_links(body, source_path, vault_path, assets_dir)
    
    # Generate title from filename if not in frontmatter
    title = frontmatter.get("title", source_path.stem.replace("-", " ").replace("_", " ").title())
    
    # Generate new frontmatter
    new_frontmatter = generate_frontmatter(frontmatter, defaults, title)
    
    # Write output
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(new_frontmatter + body, encoding="utf-8")


def main() -> None:
    """Main entry point."""
    # Paths
    repo_root = Path(__file__).parent.parent
    config_path = repo_root / "publish_config.yaml"
    
    if not config_path.exists():
        print(f"Error: Config file not found at {config_path}")
        return
    
    config = load_config(config_path)
    
    vault_path = repo_root / config["vault_path"]
    notes_dir = repo_root / "_notes"
    assets_dir = repo_root / "assets" / "images"
    
    include_patterns = config.get("include", ["**/*.md"])
    exclude_patterns = config.get("exclude", [])
    defaults = config.get("defaults", {"layout": "note"})
    
    # Clean output directory
    if notes_dir.exists():
        shutil.rmtree(notes_dir)
    notes_dir.mkdir(parents=True)
    
    # Ensure assets directory exists
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    # First pass: collect all notes for link resolution
    all_notes: dict[str, str] = {}
    notes_to_process: list[Path] = []
    
    for md_file in vault_path.rglob("*.md"):
        if should_include(md_file, vault_path, include_patterns, exclude_patterns):
            notes_to_process.append(md_file)
            note_name = md_file.stem
            slug = note_name.lower().replace(" ", "-").replace("_", "-")
            all_notes[note_name] = f"/notes/{slug}/"
    
    print(f"Found {len(notes_to_process)} notes to publish")
    
    # Second pass: process each note
    for source_path in notes_to_process:
        # Generate destination path
        slug = source_path.stem.lower().replace(" ", "-").replace("_", "-")
        dest_path = notes_dir / f"{slug}.md"
        
        process_note(source_path, dest_path, vault_path, assets_dir, defaults, all_notes)
        print(f"  ✓ {source_path.name} -> {dest_path.name}")
    
    print(f"\nSync complete! {len(notes_to_process)} notes copied to {notes_dir}")


if __name__ == "__main__":
    main()
