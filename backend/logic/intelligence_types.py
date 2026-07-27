"""Intellekt turlarining darajasini aniqlovchi so'rovnoma (Howard Gardnerning
"Multiple Intelligences" nazariyasi asosida, 10 turdagi intellekt).

MUHIM: bu test bola (7 yosh va undan katta) haqida uni yaxshi taniydigan
KATTA YOSHDAGI ikki kishi (ota-ona, vasiy, o'qituvchi yoki maktab psixologi)
tomonidan, bolani tengdoshlari bilan solishtirib to'ldirilishi uchun
mo'ljallangan — o'zi haqida o'zi to'ldirish sog'lom natija bermaydi (manba
hujjatdagi asl eslatma). Bu standart klinik kuzatuv testi ham emas; aniq
xulosa uchun klinik psixolog maslahati tavsiya etiladi.
"""
from __future__ import annotations

LIKERT: list[dict] = [
    {"value": 0, "text": "Yo'q"},
    {"value": 1, "text": "Kam"},
    {"value": 2, "text": "Ko'p"},
    {"value": 3, "text": "Juda ko'p"},
]

# Har bir toifa: label, ikon, savollar ro'yxati, o'ziga xos ball mezoni
CATEGORIES: list[dict] = [
    {
        "key": "verbal", "label": "Og'zaki intellekt", "icon": "🗣️",
        "questions": [
            "O'qish va yozishni yaxshi ko'radi",
            "So'z topish bilan bog'liq o'yinlarni yaxshi ko'radi",
            "Hazillashishni, hikoyalar o'qishni yaxshi ko'radi",
            "Ismlarni osongina o'rganadi va eslab qoladi",
            "Yoshiga nisbatan so'z boyligi yuqori (ko'p so'z biladi)",
            "O'z istaklarini bemalol ifodalaydi",
            "Ko'p gapiradi",
        ],
        "bands": [(0, 7, "Qoniqarsiz"), (8, 14, "O'rtacha"), (15, 21, "Baland")],
    },
    {
        "key": "logical", "label": "Mantiqiy intellekt", "icon": "🧮",
        "questions": [
            "Hamma narsani so'roq qiladi",
            "Buyumlarning qanday ishlashiga qiziqadi",
            "Hisoblashni yaxshi ko'radi",
            "Boshqotirma va mantiqiy o'yinlarni yaxshi ko'radi",
            "Misol-masalalarni yechishga qiziqadi",
            "Tajriba o'tkazishga qiziqadi",
            "Raqamlarni osonlik bilan o'rganadi va eslab qoladi",
        ],
        "bands": [(0, 7, "Qoniqarsiz"), (8, 14, "O'rtacha"), (15, 21, "Baland")],
    },
    {
        "key": "visual", "label": "Vizual-tasviriy intellekt", "icon": "🎨",
        "questions": [
            "Tengdoshlariga nisbatan xayolparastroq",
            "Kitob o'qish jarayonida so'zlardan ko'ra rasmlarga qiziqadi",
            "Kitob sahifalariga rasmlar chizadi",
            "San'at asarlarini yaxshi ko'radi",
            "Rasm chizish va bo'yashni yaxshi ko'radi",
            "Motivlarni chizish, misollarni topishni qoyillatadi",
            "Xarita bilan ishlashga usta",
            "Yo'l topish o'yinlarini yaxshi ko'radi",
            "Tasvirlarni yaxshi eslab qoladi",
        ],
        "bands": [(0, 9, "Qoniqarsiz"), (10, 18, "O'rtacha"), (19, 27, "Baland")],
    },
    {
        "key": "kinesthetic", "label": "Jismoniy-kinestetik intellekt", "icon": "🤸",
        "questions": [
            "Bir yoki undan ortiq sport turlarida muvaffaqiyat qozongan",
            "Uzoq vaqt bir joyda o'tira olmaydi, serharakat",
            "Har doim nimaningdir harakatida yuradi",
            "Raqs va shunga o'xshash o'yin-kulgini yaxshi ko'radi",
            "Yangi narsalarni ushlab ko'rishni, teginishni xohlaydi",
            "Gapirganda ko'pincha mimika va imo-ishoralardan foydalanadi",
            "Buzib qayta qurishni yaxshi ko'radi",
            "Harakatlanuvchi narsalarni osongina o'rganadi va eslab qoladi",
        ],
        "bands": [(0, 8, "Qoniqarsiz"), (9, 16, "O'rtacha"), (17, 24, "Baland")],
    },
    {
        "key": "musical", "label": "Musiqiy-ritmik intellekt", "icon": "🎵",
        "questions": [
            "Gapirganda ritmik gapirib, harakat qiladi",
            "Atrof-muhitdan keladigan tovushlarga sezgir",
            "Qo'shiqlarni osongina yodlab oladi va kuylaydi",
            "Musiqani yaxshi biladi",
            "Tovushlarni osongina o'rganadi va tezda eslab qoladi",
            "Xor jamoalarida ishtirok etadi, cholg'u asboblarida chaladi",
            "Tempni ushlab turishni yaxshi ko'radi",
            "Insonlarni ovozidan taniydi",
        ],
        "bands": [(0, 8, "Qoniqarsiz"), (9, 16, "O'rtacha"), (17, 24, "Baland")],
    },
    {
        "key": "social", "label": "Ijtimoiy intellekt", "icon": "🤝",
        "questions": [
            "Tengdoshlari bilan suhbatlashishdan zavqlanadi",
            "O'zini liderlardek tutadi",
            "Biron muammoga duch kelgan kishilarga yangi g'oyalar beradi",
            "Do'stona munosabatlarda hammani bir yerga jamlab turadi",
            "Tashkilotchilik qobiliyati yaxshi shakllangan",
            "Ko'pgina yaqin do'stlari bor",
            "Ko'cha hayotida mahoratli",
            "O'zini qanday himoya qilishni biladi",
            "Bir ishda vositachilik qilishga qiziqadi",
            "Do'stlarining his-tuyg'ularini yaxshi tushunadi",
        ],
        "bands": [(0, 10, "Qoniqarsiz"), (11, 20, "O'rtacha"), (21, 30, "Baland")],
    },
    {
        "key": "intrapersonal", "label": "Ichki zehn", "icon": "🪞",
        "questions": [
            "O'ziga bo'lgan ishonchi yuqori",
            "Doim o'zini tanishga harakat qiladi",
            "O'zining kuchli va zaif tomonlarini o'rganishga harakat qiladi",
            "Mustaqil harakat qilishni yaxshi ko'radi",
            "Yolg'iz ishlashni afzal ko'radi",
            "O'z oldiga maqsadlar qo'ya oladi",
            "Avval o'ylab, keyin harakat qilishni afzal ko'radi",
        ],
        "bands": [(0, 7, "Qoniqarsiz"), (8, 14, "O'rtacha"), (15, 21, "Baland")],
    },
    {
        "key": "emotional", "label": "Emotsional intellekt", "icon": "❤️",
        "questions": [
            "O'z oldiga maqsad qo'yishni biladi",
            "O'zini ruhlantira oladi",
            "Kayfiyatni tartibga solishni uddalaydi",
            "Atrofdagilar bilan yaxshi munosabat o'rnatadi",
            "O'z his-tuyg'ularini taniyoladi",
            "Boshqalarning his-tuyg'ularini tushunadi",
            "Muvaffaqiyatsizliklarni yenga oladi",
            "Emotsional hayot va voqealarni tezda o'rganadi",
            "Voqea-hodisalarni ajratish qobiliyatiga ega",
        ],
        "bands": [(0, 10, "Qoniqarsiz"), (11, 18, "O'rtacha"), (19, 27, "Baland")],
    },
    {
        "key": "moral", "label": "Axloqiy intellekt", "icon": "⚖️",
        "questions": [
            "Axloqiy me'zonlarni oson o'rganadi va qo'llaydi",
            "Ijtimoiy qoidalarga tez moslashadi",
            "Tirbandlikka tushishdek muammoga duch kelishdan yiroq",
            "Shaxsiy manfaatlariga zid bo'lsa-da axloqiy his-tuyg'ulariga ko'ra harakat qiladi",
            "Yolg'on gapirmaslikni afzal biladi",
            "Bergan va'dasining ustidan chiqadi",
            "Boshqalarning haq-huquqlarini hurmat qiladi",
            "Atrofdagilarga yordam berishga doim shay turadi",
            "Vijdon va axloq me'yorlarini ishlab chiqishga harakat qiladi",
            "Ayb ish qilganda o'zini noqulay his qiladi",
        ],
        "bands": [(0, 11, "Qoniqarsiz"), (12, 22, "O'rtacha"), (23, 30, "Baland")],
    },
    {
        "key": "naturalistic", "label": "Tabiiy intellekt", "icon": "🌿",
        "questions": [
            "Atrof-muhitni muhofaza qilishga intiladi",
            "O'simliklarni va yashilliklarni yaxshi ko'radi",
            "Hayvonlarni yaxshi ko'radi",
            "Tabiat haqida xayol suradi",
            "Tirik mavjudotlarga zarar yetkazganda, qattiq xafa bo'ladi",
            "O'zi yashayotgan joyni tabiat bilan hamohang bo'lishini istaydi",
            "Tabiat haqidagi ma'lumotlarni osongina o'rganadi va ifodalaydi",
            "Suv o'ynashni yaxshi ko'radi",
        ],
        "bands": [(0, 8, "Qoniqarsiz"), (9, 16, "O'rtacha"), (17, 24, "Baland")],
    },
]

OVERALL_LEVELS: list[dict] = [
    {"min": 0, "max": 80, "label": "Qoniqarsiz"},
    {"min": 81, "max": 120, "label": "O'rtacha"},
    {"min": 121, "max": 180, "label": "Baland"},
    {"min": 181, "max": 249, "label": "Juda baland"},
]

_TOTAL_QUESTIONS = sum(len(c["questions"]) for c in CATEGORIES)
_MAX_SCORE = _TOTAL_QUESTIONS * 3


def get_questions() -> list[dict]:
    options = [{"key": str(o["value"]), "text": o["text"]} for o in LIKERT]
    out = []
    i = 0
    for cat in CATEGORIES:
        for q in cat["questions"]:
            out.append({
                "id": i,
                "category": cat["key"],
                "categoryLabel": cat["label"],
                "prompt": q,
                "options": options,
            })
            i += 1
    return out


def _band_for(score: int, bands: list[tuple[int, int, str]]) -> str:
    for lo, hi, label in bands:
        if lo <= score <= hi:
            return label
    return bands[-1][2] if score > bands[-1][1] else bands[0][2]


def _overall_band_for(total: int) -> str:
    for level in OVERALL_LEVELS:
        if level["min"] <= total <= level["max"]:
            return level["label"]
    return OVERALL_LEVELS[-1]["label"]


def calculate(answers: list[int]) -> dict:
    if len(answers) != _TOTAL_QUESTIONS:
        raise ValueError(f"{_TOTAL_QUESTIONS} ta javob kutilgan edi, {len(answers)} ta keldi")
    for v in answers:
        if v not in {0, 1, 2, 3}:
            raise ValueError(f"Noto'g'ri javob qiymati: {v}")

    breakdown = []
    idx = 0
    total = 0
    for cat in CATEGORIES:
        n = len(cat["questions"])
        cat_score = sum(answers[idx:idx + n])
        idx += n
        total += cat_score
        breakdown.append({
            "key": cat["key"],
            "label": cat["label"],
            "icon": cat["icon"],
            "score": cat_score,
            "max": n * 3,
            "band": _band_for(cat_score, cat["bands"]),
        })

    return {
        "total": total,
        "max": _MAX_SCORE,
        "overallBand": _overall_band_for(total),
        "breakdown": breakdown,
    }
