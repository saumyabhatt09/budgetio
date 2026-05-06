# BudgetIO — Personal Budget PWA

A mobile-first Progressive Web App for tracking monthly expenses, backed by Google Sheets.

---

## Deploy to GitHub Pages (5 minutes)

### Step 1 — Push to GitHub

1. Go to **github.com** → click **New repository**
2. Name it `budgetio` (or anything you like), set it to **Public**, click **Create**
3. Upload these files:
   - `index.html`
   - `manifest.json`
   - `sw.js`
   - `icon-192.png`
   - `icon-512.png`

   Easiest way: drag and drop all files into the GitHub repo page and click **Commit changes**

### Step 2 — Enable GitHub Pages

1. In your repo → **Settings** → **Pages**
2. Under "Branch", select **main** → **/ (root)** → click **Save**
3. Wait ~60 seconds, then your app is live at:
   `https://YOUR-USERNAME.github.io/budgetio/`

---

## Set Up Google Sheets API (free)

### Step 1 — Create your Sheet

1. Go to [sheets.google.com](https://sheets.google.com)
2. Create a blank spreadsheet, name it **"Monthly Budget"**
3. Copy the **Sheet ID** from the URL:
   `https://docs.google.com/spreadsheets/d/`**`THIS_IS_YOUR_SHEET_ID`**`/edit`

### Step 2 — Get an API Key

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project (or use an existing one)
3. Go to **APIs & Services** → **Enable APIs** → search **Google Sheets API** → Enable
4. Go to **APIs & Services** → **Credentials** → **+ Create Credentials** → **API Key**
5. Copy the key, then click **Edit** → under "API restrictions" select **Google Sheets API** → Save

### Step 3 — Connect in the app

1. Open your app URL on your phone
2. Paste your **Sheet ID** and **API Key**
3. Set your monthly income → tap **Connect & Start**

---

## Install on your phone (make it a real app icon)

### iPhone / iPad
1. Open your app URL in **Safari**
2. Tap the **Share** button (box with arrow)
3. Scroll down → tap **Add to Home Screen**
4. Tap **Add** → done! BudgetIO appears as an app icon

### Android
1. Open your app URL in **Chrome**
2. Tap the **⋮ menu** (top right)
3. Tap **Add to Home screen** → **Add**
4. BudgetIO appears as an app icon

---

## Features

- **4 tabs**: Home dashboard, Add expense, Full history, Settings
- **Per-month tabs** in Google Sheets — one tab auto-created per month (e.g. `May-2026`)
- **Category budgets** — 10 categories with configurable limits
- **Progress bars** — turn amber at 70%, red at 90%
- **Savings projections** — monthly, annual, 5-year
- **Mini bar chart** — last 6 months at a glance
- **Works offline** — service worker caches the app shell
- **Remembers your settings** — Sheet ID, API key, and budgets saved in browser

---

## Data structure in Google Sheets

Each month tab has columns: `Description | Category | Amount | Date | Notes`

You can edit rows directly in the sheet — tap **↻ Refresh** in the app to sync changes back.
