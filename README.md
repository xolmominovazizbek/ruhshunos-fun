# Ruhshunos — sayt versiyasi (MVP)

Asl `@Ruhshunos_Fun loyihasi.docx` hujjatida Telegram bot sifatida rejalashtirilgan
testlarning veb-sayt versiyasi. Nom "Ruhshunos" — sayt nafaqat ko'ngilochar, balki
odamning ruhiy holatiga aniqlik kiritishga ham xizmat qilishini ta'kidlaydi.

6 ta test tayyor, ikkiga ajratilgan:

**🔬 Ilmiy asoslangan:**
- 🧩 Hissiy intellekt (EQ)
- 🌀 Stress darajasi

**✨ Qiziqarli (ko'ngilochar, ilmiy tasdiqlanmagan):**
- ♈ Munajjimlar bashorati (zodiak belgisi + juftlik mosligi)
- 🔢 Hayot soni (Pythagorean numerologiya)
- 💞 Sevgi tilingiz (5 Love Languages, Gary Chapman)
- 🧠 Temperamentingiz (Gippokrat 4 temperamenti)

To'lov va foydalanuvchi tarixi keyingi bosqichlarda qo'shiladi.

`ruhshunos-fun.html` — shu testlarning avvalgi, to'liq mustaqil (backend'siz,
bitta HTML faylga qamalgan) prototipi; hozirgi `backend/` + `frontend/`
versiyasi ushbu prototipdan portlangan va u bilan almashtirilgan.

`files/*.html` — saytning joriy vizual dizayni (pergament/oltin/teal, Fraunces +
Manrope shriftlari, 4 bo'limli navigatsiya) asos qilib olingan dastlabki maketlar.

## Ishga tushirish

```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Brauzerda `http://127.0.0.1:8000` sahifasini oching.

## Loyiha tuzilishi

```
backend/
  main.py              # FastAPI ilova va API endpoint'lari
  logic/
    zodiac.py           # zodiak belgisi va moslik hisoblash
    life_path.py        # hayot soni hisoblash
    love_language.py     # sevgi tili testi
    temperament.py       # temperament testi
    eq.py                # hissiy intellekt testi
    stress.py            # stress darajasi testi
frontend/
  index.html            # Home — bosh sahifa
  testlar.html          # Testlar — ilmiy/qiziqarli guruhlangan ro'yxat
  yaratuvchi.html        # Yaratuvchi — loyiha muallifi haqida
  yordam.html            # Yordam — kontakt va hamkorlik
  zodiac.html, life-path.html, love-language.html,
  temperament.html, eq.html, stress.html
  css/style.css
  js/quiz.js             # umumiy savol-javob (stepper) mexanizmi
  js/zodiac.js, js/life-path.js, js/love-language.js,
  js/temperament.js, js/eq.js, js/stress.js
  img/yaratuvchi.jpg     # muallif profil rasmi
```

## API

| Endpoint | Metod | Tavsif |
| --- | --- | --- |
| `/api/zodiac` | POST | Zodiak belgisi + (ixtiyoriy) juftlik moslik |
| `/api/life-path` | POST | Hayot soni hisob-kitobi |
| `/api/love-language/questions` | GET | Sevgi tili savollari |
| `/api/love-language` | POST | Sevgi tili natijasi |
| `/api/temperament/questions` | GET | Temperament savollari |
| `/api/temperament` | POST | Temperament natijasi |
| `/api/eq/questions` | GET | EQ savollari |
| `/api/eq` | POST | EQ natijasi |
| `/api/stress/questions` | GET | Stress savollari |
| `/api/stress` | POST | Stress natijasi |

## Deploy

`render.yaml` orqali Render.com'da Blueprint sifatida deploy qilingan.
Jonli sayt: https://ruhshunos-fun.onrender.com (GitHub repo va manzil nomi
tarixiy sabablarga ko'ra `ruhshunos-fun`, saytdagi ko'rinadigan nom esa
"Ruhshunos").
