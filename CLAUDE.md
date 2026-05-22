# ruhullasheik — CLAUDE.md

This is Ruhulla Sheik's GitHub profile repository. It contains:
- `README.md` — public GitHub profile page
- `docs/Ruhulla_Sheik_Resume.md` — resume source of truth (Markdown)
- `docs/Ruhulla_Sheik_Resume.pdf` — generated PDF (committed alongside MD)
- `generate_resume.py` — MD → PDF converter (headless Chromium via Playwright)

---

## Setup on a new machine

### Prerequisites
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

### Steps

```sh
git clone https://github.com/ruhullasheik/ruhullasheik.git
cd ruhullasheik

# Install Python deps
uv sync

# Install Chromium (one-time, ~300MB)
uv run playwright install chromium

# Install git hooks
sh scripts/install-hooks.sh
```

---

## Generating the PDF manually

```sh
uv run python generate_resume.py
# Output: docs/Ruhulla_Sheik_Resume.pdf
```

---

## Resume update workflow

The pre-commit hook auto-regenerates the PDF whenever `docs/Ruhulla_Sheik_Resume.md` is staged:

```sh
# 1. Edit the resume
# 2. Stage it
git add docs/Ruhulla_Sheik_Resume.md

# 3. Commit — hook fires automatically:
#    - Detects MD is staged
#    - Runs generate_resume.py
#    - Stages the new PDF
#    - Both MD + PDF are committed together
git commit -m "Update resume"

git push
```

---

## Project structure

```
ruhullasheik/
├── docs/
│   ├── Ruhulla_Sheik_Resume.md   # resume source (edit this)
│   └── Ruhulla_Sheik_Resume.pdf  # generated output (do not edit)
├── scripts/
│   ├── pre-commit                # hook source (version-controlled)
│   └── install-hooks.sh          # run once after cloning
├── generate_resume.py            # MD → PDF via Playwright + markdown
├── pyproject.toml                # uv project config + dependencies
├── uv.lock                       # locked dependencies
├── .gitignore
└── README.md                     # GitHub profile page
```

---

## Dependencies

Managed via `uv`. Defined in `pyproject.toml`:

| Package | Purpose |
|---|---|
| `markdown` | Converts MD to HTML |
| `playwright` | Headless Chromium for HTML → PDF |

> Chromium itself is installed separately via `uv run playwright install chromium` and lives in `~/.ms-playwright/` (not in the repo).
