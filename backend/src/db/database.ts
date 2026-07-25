import Database from 'better-sqlite3';
import path from 'path';

// Создаём файл базы данных dental.db рядом с проектом
const db = new Database(path.join(__dirname, '../../dental.db'));

// Создаём таблицы если их нет
db.exec(`
  CREATE TABLE IF NOT EXISTS patients (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    name      TEXT    NOT NULL,
    phone     TEXT,
    email     TEXT,
    birthdate TEXT,
    blood_type TEXT,
    allergies TEXT,
    notes     TEXT,
    created_at TEXT DEFAULT (datetime('now'))
  );

  CREATE TABLE IF NOT EXISTS appointments (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id   INTEGER REFERENCES patients(id),
    patient_name TEXT    NOT NULL,
    phone        TEXT,
    service      TEXT,
    date         TEXT    NOT NULL,
    time         TEXT    NOT NULL,
    status       TEXT    DEFAULT 'pending',
    notes        TEXT,
    created_at   TEXT    DEFAULT (datetime('now'))
  );
`);

console.log('✅ База данных готова: dental.db');

export default db;
