import express from 'express';
import cors from 'cors';
import appointmentsRouter from './routes/appointments';
import patientsRouter from './routes/patients';

const app = express();
const PORT = 3000;

// Middleware — обрабатывает JSON и разрешает запросы с PWA
app.use(cors());
app.use(express.json());

// Маршруты
app.use('/appointments', appointmentsRouter);
app.use('/patients', patientsRouter);

// Корневой маршрут — проверка что сервер живой
app.get('/', (req, res) => {
  res.json({
    message: '🦷 Dental API работает',
    endpoints: {
      'GET  /appointments':        'все записи',
      'POST /appointments':        'новая запись',
      'PATCH /appointments/:id/cancel': 'отменить запись',
      'GET  /patients':            'все пациенты',
      'POST /patients':            'новый пациент',
      'GET  /patients/:id':        'пациент + история',
    }
  });
});

app.listen(PORT, () => {
  console.log(`\n🚀 Сервер запущен: http://localhost:${PORT}`);
  console.log(`📋 Эндпоинты:`);
  console.log(`   GET  http://localhost:${PORT}/appointments`);
  console.log(`   POST http://localhost:${PORT}/appointments`);
  console.log(`   GET  http://localhost:${PORT}/patients`);
  console.log(`   POST http://localhost:${PORT}/patients\n`);
});
