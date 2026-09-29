# KALIKA.MD — AI Agent Guide & System Reference for `hrmsapp`

> **Note for AI Coding Assistants / Agents:**
> Read this document first before making ANY changes to this codebase. It defines the core architecture, non-negotiable constraints, override mechanisms, and standard operational procedures for `hrmsapp`.

---

## 1. Core Invariants & Rules (NEVER VIOLATE)

1. **Isolation from Core HRMS:**
   - **DO NOT** edit or modify anything inside `apps/hrms/`.
   - All customizations, overrides, styles, patches, and features must reside exclusively inside `apps/hrmsapp/`.

2. **No Static Asset Hashes in HTML:**
   - **DO NOT** hardcode compiled asset hashes (e.g. `index-<hash>.js`, `frappe-ui-<hash>.js`) into `hrmsapp/www/hrms.html`.
   - `hrmsapp/www/hrms.py` dynamically loads the compiled `index.html` directly from disk (`hrmsapp/public/frontend/index.html`). Hardcoding hashes will cause 404s and blank screens whenever Vite rebuilds.

3. **Vite Base Path is Mandatory:**
   - `base: "/assets/hrmsapp/frontend/"` MUST remain in `frontend/vite.config.js`.
   - Without this base path, Vite generates root-relative chunks (`/assets/...`) instead of Frappe app assets (`/assets/hrmsapp/frontend/assets/...`), breaking dynamic imports with 404s.

4. **Never Overwrite `hrmsapp/www/` with Core HRMS:**
   - **DO NOT** add `cp -r ../../hrms/hrms/www ../hrmsapp/` to build scripts. That overwrites custom templates with core Frappe HR.

5. **Git Identity & Branching:**
   - Remote URL: `https://github.com/karthik3854k/hrmsapp.git`
   - Active Branch: `develop`
   - Author: `karthik3854k` (`polisettykarthik3@gmail.com`)
   - On every change, commit and push to both `origin develop` and `upstream develop`.

---

## 2. System Architecture & Overrides Map

```
┌─────────────────────────────────────────────────────────────┐
│                       Browser / PWA                         │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    Frappe Web Server                        │
│                                                             │
│  /hrms Route ──► hrmsapp/www/hrms.py                        │
│                  ├─ Injects csrf_token, boot info, site_name│
│                  └─ Dynamically reads from disk:            │
│                     hrmsapp/public/frontend/index.html       │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                Vite Build Pipeline (frontend/)              │
│                                                             │
│  Entry: frontend/index.html                                 │
│  Plugin: srcOverridesPlugin() (in frontend/vite.config.js)   │
│                                                             │
│  For every file requested from @/ or /src/:                 │
│    IF file exists in frontend/src_overrides/                │
│       ──► COMPILE FROM frontend/src_overrides/              │
│    ELSE                                                     │
│       ──► FALLBACK TO frontend/src/                         │
└─────────────────────────────────────────────────────────────┘
```

### Key Files & Locations

| Component | Path | Purpose |
|---|---|---|
| **Vite Config** | `frontend/vite.config.js` | Configures `base`, PWA manifest, and `srcOverridesPlugin()`. |
| **Luxury Overrides** | `frontend/src_overrides/` | Contains custom luxury components, views, logos, and `main.css`. |
| **Base Source** | `frontend/src/` | Base Frappe HR frontend code. Never edit when an override can be made. |
| **Compiled Bundle** | `hrmsapp/public/frontend/` | Vite output directory (`index.html` + `assets/*.js, *.css`). |
| **Route Handler** | `hrmsapp/www/hrms.py` | Python context handler that loads `index.html` from disk dynamically. |
| **HTML Template** | `hrmsapp/www/hrms.html` | Jinja wrapper that renders `{{ app_html \| safe }}`. |
| **DocType Patches** | `hrmsapp/overrides.py` | Contains `CustomLeaveApplication` and MariaDB 12 SQL sanitizer patches. |
| **Frappe Hooks** | `hrmsapp/hooks.py` | Hooks `override_doctype_class`, `before_request`, and `template_apps`. |

---

## 3. How to Implement UI Overrides

To modify any frontend component or view:

1. **Find the original component** in `frontend/src/` (e.g. `frontend/src/components/MyComponent.vue`).
2. **Create the matching path** inside `frontend/src_overrides/` (e.g. `frontend/src_overrides/components/MyComponent.vue`).
3. **Make your changes** in `frontend/src_overrides/components/MyComponent.vue`.
4. **Rebuild the frontend bundle:**
   ```bash
   cd frontend && yarn build
   ```
5. Vite will automatically prioritize your override file over the base file.

---

## 4. MariaDB 12 Database Compatibility Engine

### The Problem
MariaDB 12 added `to_date` as a reserved keyword. Unquoted references to the `to_date` column in core queries crash with SQL syntax errors.

### The Solution (`hrmsapp/overrides.py`)
- `CustomLeaveApplication`: Explicitly backticks `` `from_date` `` and `` `to_date` `` in leave overlap validation queries.
- `patch_all()`: Monkey-patches `frappe.database.database.Database.sql` and `Database._transform_query` using regex to automatically wrap unquoted `to_date` columns in backticks:
  ```python
  TO_DATE_PATTERN = re.compile(r"(?<![`:\w])(?<!%\()(?<!%\b)\bto_date\b(?![\(`])", re.IGNORECASE)
  ```
- Hooked at runtime via `before_request = ["hrmsapp.overrides.patch_all"]` in `hooks.py`.

---

## 5. Luxury Emerald & Gold Brand Tokens

- **Brand:** Kalika Jewels
- **App Title:** `Kalika`
- **Primary Color:** Deep Royal Emerald
  - Dark: `#022c22`
  - Normal: `#064e3b`
  - Accent / Hover: `#047857`
- **Secondary / Highlight Color:** Polished Gold
  - Normal: `#d97706`
  - Accent: `#b45309`
  - Bright: `#f59e0b`
  - Light Background: `#fef3c7`
- **Logo:** `frontend/src_overrides/components/icons/FrappeHRLogo.vue` renders the Kalika Jewels emblem.

---

## 6. Standard Commands for Agents

### Rebuilding Frontend (Required after any UI changes):
```bash
cd apps/hrmsapp/frontend
yarn build
```

### Clearing Frappe Cache:
```bash
cd sites && ../env/bin/python -m frappe.utils.bench_helper frappe --site hrmsapp clear-cache
```

### Verifying Route & Bundles:
```bash
curl -s -i http://localhost:8000/hrms | grep -E "HTTP/1.1|<title>|index-.*\.js"
```

### Git Commit & Push:
```bash
git add -A
git commit -m "<type>(<scope>): <concise description>"
git push origin develop && git push upstream develop
```
