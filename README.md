# Ruhshunos — sayt versiyasi (MVP)

Asl `@Ruhshunos_Fun loyihasi.docx` hujjatida Telegram bot sifatida rejalashtirilgan
testlarning veb-sayt versiyasi. Ruhshunos — **faqat ilmiy asoslangan psixologik
testlar va tibbiy bilim testlarini** taqdim etadigan platforma. Astrologiya,
numerologiya va shunga o'xshash ilmiy asoslanmagan ko'ngilochar testlar saytda
qasddan yo'q.

**🔬 Ilmiy asoslangan psixologik testlar:**
- 🧩 Hissiy intellekt (EQ)
- ❤️ Emotsional intellekt — Nevzat Tarhan testi
- 🌀 Stress darajasi
- 🧠 Intellekt turlari so'rovnomasi (10 turdagi intellekt, bolani kuzatish uchun)
- 🔢 Shulte jadvali, 🎨 Stroop testi, 🔴 Shulte-Gorbov, ⭕ Landolt xalqalari (diqqat)
- 🔢 Digit Span, 🟢 Corsi bloklari (xotira)
- 🎭 Leonhard-Shmishek xarakter aksentuatsiyasi (88 savol, 10 shkala)
- 😰 GAD-7, 🌧️ PHQ-9, 📋 Spilberger-Xanin STAI (klinik skrining testlari)

**📖 Tibbiy bilim testlari (tibbiyot talabalari/shifokorlar uchun, ob'ektiv
to'g'ri-javobli savollar, psixologik test emas):**
- 🧠 Bosh miya nervlari (I, II, III, IV, VI juftlar)

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
  main.py                   # FastAPI ilova va API endpoint'lari
  logic/
    eq.py                   # hissiy intellekt testi
    eq_tarhan.py            # Nevzat Tarhan EQ testi
    stress.py               # stress darajasi testi
    intelligence_types.py   # 10 turdagi intellekt so'rovnomasi
    cranial_nerves.py       # bosh miya nervlari bilim testi
    leonhard_shmishek.py    # xarakter aksentuatsiyasi testi
    gad7.py                 # GAD-7 xavotir skriningi
    phq9.py                 # PHQ-9 kayfiyat skriningi
    stai.py                 # Spilberger-Xanin STAI testi
frontend/
  index.html                # Home — bosh sahifa
  testlar.html               # Testlar — toifalar bo'yicha guruhlangan ro'yxat
  yaratuvchi.html             # Yaratuvchi — loyiha muallifi haqida
  yordam.html                 # Yordam — kontakt, yordam raqamlari, hamkorlik
  maxfiylik.html               # Maxfiylik siyosati
  eq.html, eq-tarhan.html, stress.html, intelligence-types.html,
  shulte-test.html, stroop-test.html, shulte-gorbov-test.html, landolt-test.html,
  digit-span-test.html, corsi-blocks-test.html,
  leonhard-shmishek-test.html, gad7-test.html, phq9-test.html, stai-test.html,
  bosh-miya-nervlari-test.html
  css/style.css, css/disclaimer.css
  js/quiz.js                 # umumiy savol-javob (stepper) mexanizmi
  js/disclaimer.js           # markazlashtirilgan ogohlantirish/yordam matnlari
  js/<har-bir-test>.js        # test sahifasiga mos natija render qiluvchi skript
  img/yaratuvchi.jpg          # muallif profil rasmi
```

## API

| Endpoint | Metod | Tavsif |
| --- | --- | --- |
| `/api/eq/questions`, `/api/eq` | GET, POST | EQ savollari / natijasi |
| `/api/eq-tarhan/questions`, `/api/eq-tarhan` | GET, POST | Nevzat Tarhan EQ testi |
| `/api/stress/questions`, `/api/stress` | GET, POST | Stress savollari / natijasi |
| `/api/intelligence-types/questions`, `/api/intelligence-types` | GET, POST | Intellekt turlari so'rovnomasi |
| `/api/cranial-nerves/questions`, `/api/cranial-nerves` | GET, POST | Bosh miya nervlari bilim testi |
| `/api/leonhard-shmishek/questions`, `/api/leonhard-shmishek` | GET, POST | Xarakter aksentuatsiyasi testi |
| `/api/gad7/questions`, `/api/gad7` | GET, POST | GAD-7 xavotir skriningi |
| `/api/phq9/questions`, `/api/phq9` | GET, POST | PHQ-9 kayfiyat skriningi |
| `/api/stai/questions`, `/api/stai` | GET, POST | Spilberger-Xanin STAI testi |

Diqqat va xotira testlari (Shulte, Stroop, Shulte-Gorbov, Landolt, Digit Span,
Corsi bloklari) to'liq frontend tomonda ishlaydi — server bilan natija
almashinmaydi (maxfiylik siyosatiga muvofiq).

## Deploy

`render.yaml` orqali Render.com'da Blueprint sifatida deploy qilingan.
Jonli sayt: https://ruhshunos-fun.onrender.com (GitHub repo va manzil nomi
tarixiy sabablarga ko'ra `ruhshunos-fun`, saytdagi ko'rinadigan nom esa
"Ruhshunos").
