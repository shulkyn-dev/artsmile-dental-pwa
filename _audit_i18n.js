// Точный аудит переводов: реально вычисляет объект I18N и сравнивает ключи.
const fs = require('fs');
const path = require('path');
const src = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');

const m = src.match(/const I18N = (\{[\s\S]*?\n\});/);
const I18N = eval('(' + m[1] + ')');

const langs = Object.keys(I18N);
const all = new Set();
langs.forEach(l => Object.keys(I18N[l]).forEach(k => all.add(k)));
console.log('Всего уникальных ключей:', all.size);

let problems = 0;
langs.forEach(l => {
  const miss = [...all].filter(k => !(k in I18N[l]));
  console.log(`[${l}] ключей: ${Object.keys(I18N[l]).length}  пропущено: ${miss.length ? miss.join(', ') : '— нет —'}`);
  if (miss.length) problems++;
});

// HTML data-i18n покрытие
const htmlKeys = [...src.matchAll(/data-i18n(?:-html)?="([^"]+)"/g)].map(x => x[1]);
const trset = new Set(Object.keys(I18N.tr));
const badHtml = [...new Set(htmlKeys)].filter(k => !trset.has(k));
console.log(`\n[HTML data-i18n] уникальных: ${new Set(htmlKeys).size}  нет в переводах: ${badHtml.length ? badHtml.join(', ') : '— нет —'}`);
if (badHtml.length) problems++;

// t('literal') с границей слова (чтобы не путать с openSheet/get)
const tk = [...src.matchAll(/(?<![\w$])t\('([a-zA-Z_]\w*)'\)/g)].map(x => x[1]);
const badT = [...new Set(tk)].filter(k => !trset.has(k));
console.log(`[JS t('...')] литеральных: ${new Set(tk).size}  нет в переводах: ${badT.length ? badT.join(', ') : '— нет —'}`);
if (badT.length) problems++;

console.log(problems ? `\n⚠️ Проблем: ${problems}` : '\n✅ Все переводы на месте, во всех трёх языках.');
