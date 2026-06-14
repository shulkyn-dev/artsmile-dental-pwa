# 📸 Промты для генерации фото врачей (единый стиль)

Цель: 4 портрета в ОДНОМ стиле, чтобы выглядели как одна команда клиники.
Подходит для Midjourney, DALL·E, Leonardo, Flux и т.п.

## ⚙️ Как добиться единого стиля (важно!)
1. Генерь все 4 **подряд, в одной сессии**, не меняя описание стиля (блок ниже одинаковый у всех).
2. Один и тот же **фон, свет, халат, ракурс** — это уже прописано в промтах.
3. В Midjourney добавь в конце у всех одинаковый флаг: `--ar 1:1 --style raw`. Для ещё большей
   схожести можно зафиксировать сид: добавь `--seed 1234` (одинаковый у всех четырёх).
4. Сохраняй квадратом 1:1, минимум 600×600, формат **JPG**.

---

## 🔁 Общий блок стиля (он уже вшит в каждый промт ниже)
> professional medical headshot, wearing a clean white dental coat, soft light blue-grey studio
> background, bright soft diffused studio lighting, friendly confident expression, looking at the
> camera, shoulders-up portrait, sharp focus, photorealistic, 85mm lens, 1:1 square — same lighting
> and background as the other clinic doctors

---

## 1) Dr. Ahmet Yılmaz — имплантолог / хирург  →  `dr-ahmet-yilmaz.jpg`
```
Photorealistic professional medical headshot of a Turkish male dentist, around 48 years old,
distinguished, short neatly combed dark hair with slight grey at the temples, clean-shaven,
warm authoritative smile, wearing a clean white dental coat, soft light blue-grey studio
background, bright soft diffused studio lighting, looking at the camera, shoulders-up portrait,
sharp focus, 85mm lens, 1:1 square, same lighting and background as the other clinic doctors
--ar 1:1 --style raw
```

## 2) Dr. Fatma Koç — эстетическая стоматология  →  `dr-fatma-koc.jpg`
```
Photorealistic professional medical headshot of a Turkish female dentist, around 37 years old,
elegant, shoulder-length dark brown hair, subtle natural makeup, warm approachable smile,
wearing a clean white dental coat, soft light blue-grey studio background, bright soft diffused
studio lighting, looking at the camera, shoulders-up portrait, sharp focus, 85mm lens, 1:1 square,
same lighting and background as the other clinic doctors
--ar 1:1 --style raw
```

## 3) Dr. Mehmet Öztürk — ортодонт  →  `dr-mehmet-ozturk.jpg`
```
Photorealistic professional medical headshot of a Turkish male dentist, around 38 years old,
friendly and modern, neat short dark hair, wearing thin modern glasses, light stubble, warm smile,
wearing a clean white dental coat, soft light blue-grey studio background, bright soft diffused
studio lighting, looking at the camera, shoulders-up portrait, sharp focus, 85mm lens, 1:1 square,
same lighting and background as the other clinic doctors
--ar 1:1 --style raw
```

## 4) Dr. Zeynep Arslan — пародонтолог  →  `dr-zeynep-arslan.jpg`
```
Photorealistic professional medical headshot of a Turkish female dentist, around 33 years old,
professional and kind, dark hair tied back in a low neat bun, minimal makeup, confident gentle
smile, wearing a clean white dental coat, soft light blue-grey studio background, bright soft
diffused studio lighting, looking at the camera, shoulders-up portrait, sharp focus, 85mm lens,
1:1 square, same lighting and background as the other clinic doctors
--ar 1:1 --style raw
```

---

## ✅ После генерации
1. Обрежь квадратом (лицо по центру, плечи видны), сохрани как JPG с именами выше.
2. Положи 4 файла в папку `images/`.
3. Напиши мне «фото готовы» — я скопирую в деплой и обновлю сайт.

## ➕ Если захочешь добавить ещё врачей
Скажи специализацию (напр. «детский стоматолог» или «эндодонт») — я добавлю врача в приложение
(с правильной привязкой услуга→врач) и дам промт в том же стиле.
