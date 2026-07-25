# 🚀 Deploying the ArtSmile demo to Cloudflare (and generating a QR code)

The folder is ready to publish as-is. Everything is static — no server needed.

Files that get published:
- `index.html` — the app itself
- `manifest.webmanifest` — makes it "installable"
- `sw.js` — offline mode (Service Worker)
- `icon-192.png`, `icon-512.png`, `icon-maskable.png`, `apple-touch-icon.png`, `favicon.png` — icons
- (`_genicons.py` and this `DEPLOY.md` are dev-only, safe to skip uploading, but harmless if included)

---

## OPTION A — Drag and drop (simplest, 0 commands) ⭐

1. Go to **https://dash.cloudflare.com/** → **Workers & Pages**.
2. Click **Create** → **Pages** tab → **Upload assets**.
3. Name the project, e.g. `artsmile-demo`.
4. **Drag the whole folder** `dental_pwa_demo` into the upload window (or select the files).
5. Click **Deploy site**.
6. In ~20 seconds you'll get a link like:
   `https://artsmile-demo.pages.dev`

Done. Open that link on a phone → "Add to Home Screen".

---

## OPTION B — Via wrangler (terminal)

```powershell
# 1. Log in to Cloudflare (opens a browser, click Allow)
npx wrangler login

# 2. Deploy the folder (run from the project folder)
npx wrangler pages deploy . --project-name=artsmile-demo
```

---

## After deploying — generate a QR code for the front desk

Once you have the link (e.g. `https://artsmile-demo.pages.dev`), generate a printable QR PNG:

```powershell
python make_qr.py https://artsmile-demo.pages.dev
```

Patient scans it → app opens → adds it to their phone.

---

## ⚠️ Important note on installability
"Add to Home Screen" (full app mode, icon, offline support) **only works over HTTPS**.
Locally (`localhost`) it works partially. Cloudflare provides HTTPS automatically, so
installability works right after deployment.
