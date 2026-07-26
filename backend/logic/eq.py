"""Hissiy intellekt (EQ) — 5 ballik Likert shkalasi asosidagi test.

Manba: ruhshunos-fun.html standalone prototipidan portlangan (JS -> Python),
mazmuni o'zgarishsiz saqlangan.
"""
from __future__ import annotations

EQ_LIKERT: list[dict] = [
    {"value": 1, "text": "Mutlaqo unday emas"},
    {"value": 2, "text": "Ko'pincha unday emas"},
    {"value": 3, "text": "Qisman shunday"},
    {"value": 4, "text": "Ko'pincha shunday"},
    {"value": 5, "text": "Menga juda mos"},
]

EQ_CATEGORIES: dict[str, str] = {
    "selfAwareness": "O'z-o'zini anglash",
    "selfRegulation": "O'zini boshqarish",
    "empathy": "Empatiya",
    "socialSkills": "Ijtimoiy ko'nikmalar",
}

EQ_QUESTIONS: list[dict] = [
    {"category": "selfAwareness", "prompt": "O'zimning kuchli va zaif tomonlarimni aniq bilaman."},
    {"category": "selfAwareness", "prompt": "Hissiyotlarim paydo bo'lgan zahoti ularni farqlay olaman."},
    {"category": "selfAwareness", "prompt": "Nima meni asabiylashtirishini yoki xursand qilishini aniq bilaman."},
    {"category": "selfAwareness", "prompt": "O'z xatti-harakatlarim boshqalarga qanday ta'sir qilishini tushunaman."},
    {"category": "selfAwareness", "prompt": "Kayfiyatim ish yoki qarorlarimga qay darajada ta'sir qilishini bilaman."},
    {"category": "selfRegulation", "prompt": "G'azablanganimda ham xotirjamlikni saqlashga harakat qilaman."},
    {"category": "selfRegulation", "prompt": "Qiyin vaziyatlarda shoshilinch qaror qabul qilishdan saqlanaman."},
    {"category": "selfRegulation", "prompt": "Stressli holatlarda o'zimni tez tinchlantira olaman."},
    {"category": "selfRegulation", "prompt": "Va'da bergan narsalarimni bajarishga intizom bilan yondashaman."},
    {"category": "selfRegulation", "prompt": "Tanqidga darhol himoyalanish bilan emas, xotirjamlik bilan javob beraman."},
    {"category": "empathy", "prompt": "Boshqalarning his-tuyg'ularini so'zsiz ham sezib olaman."},
    {"category": "empathy", "prompt": "Suhbatdoshim gapirganda uni to'liq diqqat bilan tinglayman."},
    {"category": "empathy", "prompt": "Boshqa odamning nuqtai nazaridan qarashga harakat qilaman."},
    {"category": "empathy", "prompt": "Kimdir qiynalganda buni sezib, unga yordam berishga intilaman."},
    {"category": "empathy", "prompt": "Turli fikr va his-tuyg'ularga hurmat bilan qarayman."},
    {"category": "socialSkills", "prompt": "Yangi odamlar bilan tez til topisha olaman."},
    {"category": "socialSkills", "prompt": "Ziddiyatli vaziyatlarda muloqot orqali yechim topishga harakat qilaman."},
    {"category": "socialSkills", "prompt": "Jamoada ishlashda boshqalarni rag'batlantira olaman."},
    {"category": "socialSkills", "prompt": "Fikrlarimni aniq va tushunarli tarzda yetkaza olaman."},
    {"category": "socialSkills", "prompt": "Boshqalar bilan ishonchli munosabatlar qura olaman."},
]

EQ_LEVELS: list[dict] = [
    {"min": 20, "max": 39, "label": "Rivojlantirish kerak",
     "summary": "Hissiy intellekt ko'nikmalaringiz hali rivojlanish bosqichida — bu odatiy holat va mashq bilan yaxshilanadi.",
     "advice": [
         "Har kuni his-tuyg'ularingizni bir necha so'z bilan yozib borish (kundalik) o'z-o'zini anglashni kuchaytiradi",
         "Suhbatda gapirishdan oldin bir necha soniya to'xtab, javobingizni o'ylab ko'ring",
         "Boshqalarni to'xtatmasdan oxirigacha tinglashni mashq qiling",
     ]},
    {"min": 40, "max": 59, "label": "O'rtacha",
     "summary": "Hissiy intellektingiz o'rtacha darajada — ba'zi ko'nikmalar kuchli, ba'zilari rivojlanishga muhtoj.",
     "advice": [
         "Eng past ball to'plagan yo'nalishga alohida e'tibor qarating",
         "Ziddiyatli vaziyatlarda darhol reaksiya bildirishdan oldin chuqur nafas oling",
         "Har kuni kamida bitta suhbatda faol tinglashni mashq qiling",
     ]},
    {"min": 60, "max": 79, "label": "Yaxshi",
     "summary": "Hissiy intellektingiz yaxshi darajada — his-tuyg'ularingizni va boshqalarnikini anglay olasiz.",
     "advice": [
         "Kuchli tomonlaringizni jamoaviy ishlarda yetakchilik qilish uchun ishlating",
         "Stressli vaziyatlarda ham xotirjamligingizni saqlashni davom ettiring",
         "Boshqalarga ham hissiy ko'nikmalarni rivojlantirishda yordam bering",
     ]},
    {"min": 80, "max": 100, "label": "Yuqori",
     "summary": "Hissiy intellektingiz yuqori darajada — his-tuyg'ularni boshqarish va boshqalar bilan chuqur aloqa o'rnatishda mohirsiz.",
     "advice": [
         "Bu kuchli tomoningizni mentorlik yoki yetakchilik rolida qo'llang",
         "Boshqalarga hissiy qo'llab-quvvatlash ko'rsatishda davom eting, lekin o'zingizni ham unutmang",
         "Murakkab jamoaviy vaziyatlarda vositachi rolini o'ynashingiz mumkin",
     ]},
]


def get_questions() -> list[dict]:
    options = [{"key": str(o["value"]), "text": o["text"]} for o in EQ_LIKERT]
    return [
        {"id": i, "prompt": q["prompt"], "options": options}
        for i, q in enumerate(EQ_QUESTIONS)
    ]


def _level_for(score: int) -> dict:
    for level in EQ_LEVELS:
        if level["min"] <= score <= level["max"]:
            return level
    return EQ_LEVELS[-1]


def calculate(answers: list[int]) -> dict:
    if len(answers) != len(EQ_QUESTIONS):
        raise ValueError(f"{len(EQ_QUESTIONS)} ta javob kutilgan edi, {len(answers)} ta keldi")
    for v in answers:
        if v not in {1, 2, 3, 4, 5}:
            raise ValueError(f"Noto'g'ri javob qiymati: {v}")

    cat_totals = {key: 0 for key in EQ_CATEGORIES}
    overall = 0
    for i, value in enumerate(answers):
        overall += value
        cat_totals[EQ_QUESTIONS[i]["category"]] += value

    level = _level_for(overall)
    breakdown = [
        {"key": key, "label": label, "score": cat_totals[key], "max": 25, "pct": round(cat_totals[key] / 25 * 100)}
        for key, label in EQ_CATEGORIES.items()
    ]

    return {
        "overall": overall,
        "min": 20,
        "max": 100,
        "level": level["label"],
        "summary": level["summary"],
        "advice": level["advice"],
        "breakdown": breakdown,
    }
