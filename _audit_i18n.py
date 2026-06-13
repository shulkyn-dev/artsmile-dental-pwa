"""Аудит переводов: сравнивает ключи tr/ru/en в I18N, ищет пропуски."""
import re, os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
src = open(path, encoding="utf-8").read()

# вырезаем блок const I18N = { ... };
m = re.search(r"const I18N = \{(.*?)\n\};", src, re.S)
block = m.group(1)

# делим на языковые секции: tr: { ... }, ru: { ... }, en: { ... }
langs = {}
for lang in ["tr", "ru", "en"]:
    lm = re.search(r"\n  %s: \{(.*?)\n  \}" % lang, block, re.S)
    body = lm.group(1)
    # ключи = идентификатор в начале строки (с отступом) перед двоеточием
    keys = re.findall(r"\n    ([a-zA-Z_]\w*)\s*:", body)
    langs[lang] = keys

all_keys = set()
for l in langs:
    all_keys |= set(langs[l])

print("Всего уникальных ключей:", len(all_keys))
for lang in ["tr", "ru", "en"]:
    s = set(langs[lang])
    missing = sorted(all_keys - s)
    dups = sorted(k for k in set(langs[lang]) if langs[lang].count(k) > 1)
    print("\n[%s] ключей: %d" % (lang, len(s)))
    print("  ПРОПУЩЕНО:", missing if missing else "— нет —")
    if dups:
        print("  ДУБЛИ КЛЮЧЕЙ:", dups)

# проверка: все data-i18n / data-i18n-html в HTML существуют в tr
html_keys = set(re.findall(r'data-i18n(?:-html)?="([^"]+)"', src))
tr_keys = set(langs["tr"])
bad_html = sorted(k for k in html_keys if k not in tr_keys)
print("\n[HTML data-i18n] использовано ключей:", len(html_keys))
print("  НЕТ В ПЕРЕВОДАХ:", bad_html if bad_html else "— нет —")

# статические t('xxx') в JS (без конкатенации) — извлекаем литералы
t_keys = set(re.findall(r"t\('([a-zA-Z_]\w*)'\)", src))
bad_t = sorted(k for k in t_keys if k not in tr_keys)
print("\n[JS t('...')] литеральных ключей:", len(t_keys))
print("  НЕТ В ПЕРЕВОДАХ:", bad_t if bad_t else "— нет —")
