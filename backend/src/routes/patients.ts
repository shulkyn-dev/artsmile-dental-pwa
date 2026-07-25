import { Router, Request, Response } from 'express';
import db from '../db/database';

const router = Router();

// GET /patients — все пациенты
router.get('/', (req: Request, res: Response) => {
  const patients = db.prepare('SELECT * FROM patients ORDER BY name').all();
  res.json({ success: true, data: patients });
});

// POST /patients — новый пациент
router.post('/', (req: Request, res: Response) => {
  const { name, phone, email, birthdate, blood_type, allergies, notes } = req.body;

  if (!name) {
    res.status(400).json({ success: false, error: 'Имя обязательно' });
    return;
  }

  const result = db.prepare(`
    INSERT INTO patients (name, phone, email, birthdate, blood_type, allergies, notes)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `).run(name, phone, email, birthdate, blood_type, allergies, notes);

  res.status(201).json({
    success: true,
    message: 'Пациент добавлен',
    id: result.lastInsertRowid
  });
});

// GET /patients/:id — один пациент + его история записей
router.get('/:id', (req: Request, res: Response) => {
  const { id } = req.params;
  const patient = db.prepare('SELECT * FROM patients WHERE id = ?').get(id);

  if (!patient) {
    res.status(404).json({ success: false, error: 'Пациент не найден' });
    return;
  }

  const history = db.prepare(
    'SELECT * FROM appointments WHERE patient_id = ? ORDER BY date DESC'
  ).all(id);

  res.json({ success: true, data: { patient, history } });
});

export default router;
