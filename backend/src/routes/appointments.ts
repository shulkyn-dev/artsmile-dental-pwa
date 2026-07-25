import { Router, Request, Response } from 'express';
import db from '../db/database';

const router = Router();

// GET /appointments — все записи
router.get('/', (req: Request, res: Response) => {
  const appointments = db.prepare('SELECT * FROM appointments ORDER BY date, time').all();
  res.json({ success: true, data: appointments });
});

// POST /appointments — новая запись
router.post('/', (req: Request, res: Response) => {
  const { patient_name, phone, service, date, time, notes } = req.body;

  // Валидация — проверяем обязательные поля
  if (!patient_name || !date || !time) {
    res.status(400).json({ success: false, error: 'Обязательные поля: patient_name, date, time' });
    return;
  }

  // Проверяем что дата не в прошлом
  if (new Date(date) < new Date(new Date().toDateString())) {
    res.status(400).json({ success: false, error: 'Нельзя записаться на прошедшую дату' });
    return;
  }

  // Проверяем что слот свободен (нет другой активной записи на это время)
  const conflict = db.prepare(`
    SELECT id FROM appointments
    WHERE date = ? AND time = ? AND status != 'cancelled'
  `).get(date, time);

  if (conflict) {
    res.status(409).json({ success: false, error: 'Это время уже занято, выберите другое' });
    return;
  }

  const result = db.prepare(`
    INSERT INTO appointments (patient_name, phone, service, date, time, notes)
    VALUES (?, ?, ?, ?, ?, ?)
  `).run(patient_name, phone, service, date, time, notes);

  res.status(201).json({
    success: true,
    message: 'Запись создана',
    id: result.lastInsertRowid
  });
});

// GET /appointments/slots?date=2026-07-20 — свободные слоты на дату
router.get('/slots', (req: Request, res: Response) => {
  const { date } = req.query as { date: string };

  if (!date) {
    res.status(400).json({ success: false, error: 'Укажи дату: ?date=2026-07-20' });
    return;
  }

  // Все возможные слоты рабочего дня
  const allSlots = ['09:00','09:30','10:00','10:30','11:00','11:30',
                    '13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30'];

  // Занятые слоты на эту дату
  const taken = db.prepare(`
    SELECT time FROM appointments WHERE date = ? AND status != 'cancelled'
  `).all(date).map((r: any) => r.time);

  const free = allSlots.filter(s => !taken.includes(s));

  res.json({ success: true, date, free, taken });
});

// PATCH /appointments/:id/cancel — отменить запись
router.patch('/:id/cancel', (req: Request, res: Response) => {
  const { id } = req.params;
  db.prepare('UPDATE appointments SET status = ? WHERE id = ?').run('cancelled', id);
  res.json({ success: true, message: `Запись #${id} отменена` });
});

export default router;
