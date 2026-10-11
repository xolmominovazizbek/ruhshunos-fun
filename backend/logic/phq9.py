"""PHQ-9 (Patient Health Questionnaire-9) — kayfiyat/depressiya skriningi.

Muallif: Spitzer, Williams, Kroenke va boshq. (2001). Dunyoda eng ko'p
qo'llaniladigan standart depressiya skrining so'rovnomasi. 9 ta savol,
har biri 0-3 ball, jami 0-27.

MUHIM XAVFSIZLIK IZOHI: 9-savol o'z joniga qasd qilish/o'zига zarar
yetkazish haqidagi fikrlarni so'raydi. Agar foydalanuvchi bu savolga
0 dan yuqori ball bersa (ya'ni "hech qachon" dan boshqa har qanday
javob), natija javobida bu alohida, aniq belgilanadi — front-end bu
holatda umumiy ball qanday bo'lishidan qat'i nazar yordam raqamlarini
albatta ko'rsatishi SHART. Bu tashxis vositasi emas, lekin bu bitta
savol bo'yicha "ehtiyot chorasi yo'q" deb o'tkazib yuborish mumkin emas.
"""
from __future__ import annotations

LIKERT: list[dict] = [
    {"value": 0, "text": "Hech qachon"},
    {"value": 1, "text": "Bir necha kunda bir"},
    {"value": 2, "text": "Kunlarning yarmidan ko'pi"},
    {"value": 3, "text": "Deyarli har kuni"},
]

QUESTIONS: list[str] = [
    "Sodir bo'layotgan voqealarga qiziqish yo'qligi yoki ulardan zavq olmaslik",
    "Befarqlik, tushkunlik yoki umidsizlik hissi",
    "Uyqu bilan bog'liq muammolar — uxlashga qiynalish, uyqusizlik yoki aksincha, juda ko'p uxlash",
    "Charchoq hissi yoki kuch-quvvat yo'qotish",
    "Ishtahaning kamligi yoki aksincha, ortiqcha ovqatlanish",
    "O'zingizni yomon his qilish — muvaffaqiyatsiz yoki oilangizni/o'zingizni xafa qilgandek his qilish",
    "Kitob o'qish, televizor ko'rish kabi oddiy ishlarga e'tiborni jamlash qiyinligi",
    "G'ayrioddiy sekin harakat qilish yoki gapirish, yoki aksincha, odatdagidan ko'proq bezovta/serharakat bo'lish",
    "O'z joningizga qasd qilish yoki o'zingizga biror tarzda zarar yetkazish haqidagi fikrlar",
]

# 0-asosli indeks: oxirgi savol (9-savol) — xavfsizlik uchun alohida nazorat qilinadi.
SAFETY_ITEM_INDEX = 8

LEVELS: list[dict] = [
    {"min": 0, "max": 4, "label": "Minimal", "summary": "Depressiya belgilari deyarli yo'q."},
    {"min": 5, "max": 9, "label": "Yengil", "summary": "Yengil darajadagi kayfiyat tushishi belgilari bor."},
    {"min": 10, "max": 14, "label": "O'rtacha", "summary": "O'rtacha darajadagi belgilar — psixolog yoki psixiatr bilan suhbat tavsiya etiladi."},
    {"min": 15, "max": 19, "label": "O'rtacha og'ir", "summary": "Sezilarli darajadagi belgilar — mutaxassis yordami tavsiya etiladi."},
    {"min": 20, "max": 27, "label": "Og'ir", "summary": "Yuqori darajadagi belgilar — iloji boricha tezroq psixiatr bilan maslahatlashing."},
]


def get_questions() -> list[dict]:
    options = [{"key": str(o["value"]), "text": o["text"]} for o in LIKERT]
    return [{"id": i, "prompt": f"So'nggi 2 hafta ichida qanchalik tez-tez quyidagi holat sizni bezovta qildi: {q.lower()}", "options": options} for i, q in enumerate(QUESTIONS)]


def _level_for(total: int) -> dict:
    for level in LEVELS:
        if level["min"] <= total <= level["max"]:
            return level
    return LEVELS[-1]


def calculate(answers: list[int]) -> dict:
    if len(answers) != len(QUESTIONS):
        raise ValueError(f"{len(QUESTIONS)} ta javob kutilgan edi, {len(answers)} ta keldi")
    for v in answers:
        if v not in {0, 1, 2, 3}:
            raise ValueError(f"Noto'g'ri javob qiymati: {v}")

    total = sum(answers)
    level = _level_for(total)
    safety_flag = answers[SAFETY_ITEM_INDEX] > 0

    return {
        "total": total,
        "min": 0,
        "max": 27,
        "level": level["label"],
        "summary": level["summary"],
        "clinicalCutoff": total >= 10,
        "safetyFlag": safety_flag,
        "source": "PHQ-9 (Spitzer, Williams, Kroenke va boshq., 2001)",
    }
