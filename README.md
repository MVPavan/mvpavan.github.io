# MVPavan's Technical Notes

> 🌐 **Live Site**: [mvpavan.github.io](https://mvpavan.github.io/)

A personal knowledge base built with **Quartz 4** and **Obsidian**, automatically deployed to GitHub Pages.

---

## 🏗️ Architecture Overview

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│    Obsidian     │ ──▶ │  GitHub Actions  │ ──▶ │  GitHub Pages   │
│  (Write Notes)  │     │  (Build & Deploy)│     │  (Host Website) │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
              ┌─────▼─────┐      ┌──────▼──────┐
              │ Preprocess│      │ Quartz Build│
              │  Script   │      │   (SSG)     │
              └───────────┘      └─────────────┘
```

## 📁 Repository Structure

```
mvpavan.github.io/
├── content/                  # 📝 Your notes (Obsidian vault)
│   ├── index.md             # Homepage
│   ├── AI/                  # Topic folders
│   │   ├── EfficientML/
│   │   │   ├── attachments/ # Images for this section
│   │   │   └── *.md         # Notes
│   │   └── ...
│   └── Programming/
│       └── ...
├── quartz/                   # Quartz framework (don't edit)
├── quartz.config.ts          # ⚙️ Site configuration
├── quartz.layout.ts          # 🎨 Layout configuration
├── scripts/
│   └── preprocess_obsidian.py  # Obsidian → Quartz transformer
├── .github/workflows/
│   └── deploy.yml            # 🚀 CI/CD pipeline
└── package.json              # Node.js dependencies
```

---

## 🚀 Quick Start: Replicate This Setup

### Prerequisites
- [Node.js](https://nodejs.org/) v22+
- [Python](https://python.org/) 3.11+
- [Git](https://git-scm.com/)
- [Obsidian](https://obsidian.md/) (optional, for editing)

### Step 1: Fork or Clone Quartz

```bash
# Option A: Use this repo as template
git clone https://github.com/MVPavan/mvpavan.github.io.git my-notes
cd my-notes

# Option B: Start fresh with Quartz
npx quartz create
```

### Step 2: Install Dependencies

```bash
npm install
```

### Step 3: Configure Your Site

Edit `quartz.config.ts`:

```typescript
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Your Site Title",
    baseUrl: "yourusername.github.io",
    // ... other settings
  },
}
```

### Step 4: Add Your Notes

Place your markdown files in the `content/` directory:

```bash
content/
├── index.md          # Required: Your homepage
└── Your-Topic/
    ├── Note.md
    └── attachments/  # Images for this section
        └── image.png
```

### Step 5: Local Development

```bash
npx quartz build --serve
# Open http://localhost:8080
```

---

## 📝 Writing Notes with Obsidian

### Recommended Obsidian Settings

1. **Files & Links** → Set attachment folder to `attachments` (relative to note)
2. **Files & Links** → Enable "Automatically update internal links"
3. Open the `content/` folder as your Obsidian vault

### Supported Syntax

| Feature | Syntax | Example |
|---------|--------|---------|
| WikiLinks | `[[Note]]` | `[[Quantization]]` |
| Aliases | `[[Note\|Display]]` | `[[Quantization\|Quant]]` |
| Images | `![[image.png]]` | `![[diagram.png]]` |
| Headings | `[[#Section]]` | `[[#Overview]]` |
| Tags | `#tag` | `#ai #ml` |
| Callouts | `> [!note]` | `> [!warning] Be careful` |
| LaTeX | `$...$` or `$$...$$` | `$E = mc^2$` |

---

## 🔧 Preprocessing Script

The `scripts/preprocess_obsidian.py` script transforms Obsidian-specific syntax for Quartz compatibility.

### What It Does

| Transformation | Before | After |
|----------------|--------|-------|
| File renaming | `My Note.md` | `My-Note.md` |
| Image links | `![](attachments/img.png)` | `![[img.png]]` |
| WikiLinks | `[[My Note]]` | `[[My-Note]]` |
| Nested headings | `[[#A#B]]` | `[[#B]]` |
| Tabs → Spaces | `\t- item` | `  - item` |
| Broken assets | Searches & moves | Fixed links |

### Run Manually

```bash
python scripts/preprocess_obsidian.py content
```

---

## 🚀 Deployment

### Automatic (GitHub Actions)

Every push to `main` triggers the workflow:

1. **Checkout** → Fetches full git history
2. **Preprocess** → Runs `preprocess_obsidian.py`
3. **Build** → Runs `npx quartz build`
4. **Deploy** → Uploads to GitHub Pages

### GitHub Pages Setup

1. Go to **Settings → Pages**
2. Set Source to **GitHub Actions**
3. Push to `main` and the site will deploy

### Manual Build

```bash
# Build static site
npx quartz build

# Output is in public/
```

---

## ⚙️ Configuration Reference

### `quartz.config.ts`

```typescript
configuration: {
  pageTitle: "Site Title",           // Browser tab title
  baseUrl: "username.github.io",     // Your domain
  ignorePatterns: ["private", ...],  // Folders to exclude
  theme: { ... },                    // Colors, fonts
},
plugins: {
  transformers: [...],  // Markdown processing
  filters: [...],       // Content filtering
  emitters: [...],      // Output generation
}
```

### Key Plugins

| Plugin | Purpose |
|--------|---------|
| `ObsidianFlavoredMarkdown` | WikiLinks, callouts |
| `SyntaxHighlighting` | Code blocks |
| `Latex` | Math equations |
| `TableOfContents` | Auto TOC |
| `CrawlLinks` | Link resolution |

---

## 🎨 Customization

### Theme Colors

Edit `quartz.config.ts` → `theme.colors`:

```typescript
colors: {
  lightMode: {
    light: "#faf8f8",      // Background
    secondary: "#284b63",  // Links
    // ...
  },
  darkMode: { ... }
}
```

### Layout

Edit `quartz.layout.ts` to customize:
- Header components
- Sidebar content
- Footer

---

## 📋 Common Tasks

### Add a New Section

```bash
mkdir -p content/NewTopic/attachments
echo "---\ntitle: New Topic\n---\n\n# New Topic" > content/NewTopic/index.md
```

### Exclude a Folder from Build

Add to `ignorePatterns` in `quartz.config.ts`:

```typescript
ignorePatterns: ["private", "drafts", "YourFolder"],
```

### Fix Broken Image Links

```bash
python scripts/preprocess_obsidian.py content
# Will automatically move assets to correct locations
```

---

## 🔗 Resources

- [Quartz Documentation](https://quartz.jzhao.xyz/)
- [Obsidian Help](https://help.obsidian.md/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

---

## 📄 License

MIT License - See [LICENSE](LICENSE)