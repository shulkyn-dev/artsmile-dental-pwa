# ArtSmile Backend

Node.js + TypeScript + Express API backing the ArtSmile PWA — the piece that turns the
static frontend demo into a real, working booking system.

## Stack

`Node.js` · `TypeScript` · `Express 5` · `better-sqlite3` · `cors`

## Endpoints

| Method | Route | What it does |
|---|---|---|
| GET | `/appointments` | List all appointments |
| POST | `/appointments` | Create a new appointment |
| PATCH | `/appointments/:id/cancel` | Cancel an appointment |
| GET | `/patients` | List all patients |
| POST | `/patients` | Create a new patient |
| GET | `/patients/:id` | Patient details + treatment history |

## Running locally

```bash
npm install
npm run dev      # nodemon + ts-node, auto-reload on changes
```

Production build:
```bash
npm run build     # compiles to dist/
npm start          # runs the compiled build
```

Server listens on `http://localhost:3000`. SQLite database file is created automatically
on first run (`database.ts`).
