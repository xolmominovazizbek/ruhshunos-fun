# Ruhshunos — sayt versiyasi (MVP)

Asl `@Ruhshunos_Fun loyihasi.docx` hujjatida Telegram bot sifatida rejalashtirilgan
testlarning veb-sayt versiyasi. Ruhshunos — ikki toifa foydalanuvchiga mo'ljallangan
ilmiy platforma:

- **O'z holatini tushunmoqchi bo'lganlar** uchun — ilmiy asoslangan o'z-o'zini
  baholash testlari ("Testlar" bo'limi).
- **Tibbiyot talabalari** (bakalavr, ordinator, rezident, magistr, doktorant) va
  **soha mutaxassislari** (psixiatr, narkolog, nevropatolog, psixoterapevt, tibbiy
  psixolog, suitsidolog) uchun — bilim testlari va klinik tasnif ko'rsatmalari
  ("Fanga doir testlar", XKT-10, XKT-11 bo'limlari).

## Bo'limlar

**🔬 Testlar — ilmiy asoslangan psixologik o'z-o'zini baholash:**
- 🧩 Hissiy intellekt (EQ)
- ❤️ Emotsional intellekt — Nevzat Tarhan testi
- 🌀 Stress darajasi
- 🧠 Intellekt turlari so'rovnomasi (10 turdagi intellekt, bolani kuzatish uchun)
- 🔢 Shulte jadvali, 🎨 Stroop testi, 🔴 Shulte-Gorbov, ⭕ Landolt xalqalari (diqqat)
- 🔢 Digit Span, 🟢 Corsi bloklari (xotira)
- 🎭 Leonhard-Shmishek xarakter aksentuatsiyasi (88 savol, 10 shkala)
- 😰 GAD-7, 🌧️ PHQ-9, 📋 Spilberger-Xanin STAI, 🩺 HADS (klinik skrining testlari)

**📖 Fanga doir testlar — ob'ektiv bilim savollari, psixologik test emas:**
- 🧠 Bosh miya nervlari (I, II, III, IV, VI juftlar) — 50 savol
- 🧩 Demensiya — tasnifi, diagnostikasi, davolash (10 bob, 1269 savol)

**XKT-10 / XKT-11** — ICD-10 va ICD-11 (6-bob) tashxis kodlarini bosqichma-bosqich
qidirish uchun interaktiv "kod qulfi" vositalari.

To'lov va foydalanuvchi tarixi keyingi bosqichlarda qo'shiladi.

`ruhshunos-fun.html` — shu testlarning avvalgi, to'liq mustaqil (backend'siz,
bitta HTML faylga qamalgan) prototipi; hozirgi `backend/` + `frontend/`
versiyasi ushbu prototipdan portlangan va u bilan almashtirilgan.

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
    hads.py                 # HADS xavotir/depressiya shkalasi
frontend/
  index.html                 # Home — bosh sahifa
  testlar.html                # Testlar — psixologik o'z-o'zini baholash testlari
  fanga-doir-testlar.html      # Fanga doir testlar — tibbiy bilim testlari
  xkt-10.html, xkt-11.html      # ICD-10 / ICD-11 kod qulfi vositalari
  demensiya-test.html            # Demensiya bilim testi (o'z mustaqil dvigatelida)
  tuzuvchilar.html                # Tuzuvchilar — muallif, kontakt, yordam
  maxfiylik.html                   # Maxfiylik siyosati
  eq.html, eq-tarhan.html, stress.html, intelligence-types.html,
  shulte-test.html, stroop-test.html, shulte-gorbov-test.html, landolt-test.html,
  digit-span-test.html, corsi-blocks-test.html,
  leonhard-shmishek-test.html, gad7-test.html, phq9-test.html, stai-test.html,
  hads-test.html, bosh-miya-nervlari-test.html
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
| `/api/hads/questions`, `/api/hads` | GET, POST | HADS xavotir/depressiya shkalasi |

Diqqat va xotira testlari (Shulte, Stroop, Shulte-Gorbov, Landolt, Digit Span,
Corsi bloklari), XKT-10/XKT-11 kod qulfi vositalari va Demensiya bilim testi
to'liq frontend tomonda ishlaydi — server bilan natija almashinmaydi (XKT va
Demensiya o'z holatini brauzer `localStorage`'ida saqlaydi).

## Deploy

`render.yaml` orqali Render.com'da Blueprint sifatida deploy qilingan.
Jonli sayt: https://ruhshunos-fun.onrender.com (GitHub repo va manzil nomi
tarixiy sabablarga ko'ra `ruhshunos-fun`, saytdagi ko'rinadigan nom esa
"Ruhshunos").
