# 🦷 ArtSmile — Dental Clinic PWA Demo

A booking demo for dental clinics — a **Progressive Web App**, no app stores involved:
the patient opens a link, adds it to the home screen with one tap, and uses it like a
regular app from then on.

Built as a sales demo for cold outreach to Turkish dental clinics — show the result in
30 seconds via a link instead of describing it in words.

## What's inside

- Booking flow: service → doctor → time slot, aware of which doctors offer which service
- Patient profile: personal info, medical record, treatment history with doctor's notes, loyalty program
- Doctor cards: photo, bio, reviews, service list — expand on tap
- One-tap emergency booking for acute pain
- Dark theme (toggle in the header, persisted in localStorage)
- Home screen install: custom flow for iOS Safari (hint banner) and desktop
- Multi-language (built for the Turkish market)
- Service Worker with auto-update (`sw.js`, cache versioning)

## Technical details that usually get skipped in PWA demos

- `position: fixed` for the bottom nav bar, specifically patched for iOS Safari
  (standard `100dvh` "floats" there, had to pin the height via `window.innerHeight` in JS)
- `manifest.webmanifest` with a unique `id` — so Chrome doesn't treat a reinstall as a new app
- Safe-area padding for the iPhone notch / gesture bar

## Stack

Plain **HTML/CSS/JS**, no framework — a deliberate choice, so the demo weighs almost
nothing and opens instantly on slow mobile connections (a common scenario for a clinic's
end clients). Hosted on Cloudflare Pages.

## Running locally

```bash
npx serve -p 3456 .
```

Or just open `index.html` in a browser — the app is fully static, no backend required
(data is mocked, baked into the JS).

## Deployment

See [DEPLOY.md](DEPLOY.md) — Cloudflare Pages, `public/` is built from the source files.
