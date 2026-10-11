"""GAD-7 (Generalized Anxiety Disorder 7-item scale) — umumiy xavotir skriningi.

Muallif: Spitzer, Kroenke, Williams, Löwe (2006). Bu dunyoda eng ko'p
qo'llaniladigan, validatsiyadan o'tgan standart xavotir skrining
so'rovnomalaridan biri. 7 ta savol, har biri 0-3 ball, jami 0-21.

MUHIM: bu skrining vositasi, tashxis quroli emas. Yuqori ball klinik
suhbat va mutaxassis xulosasini talab qiladi.
"""
from __future__ import annotations

LIKERT: list[dict] = [
    {"value": 0, "text": "Hech qachon"},
    {"value": 1, "text": "Bir necha kunda bir"},
    {"value": 2, "text": "Kunlarning yarmidan ko'pi"},
    {"value": 3, "text": "Deyarli har kuni"},
]

QUESTIONS: list[str] = [
    "Asabiy qo'zg'aluvchanlik, bezovtalik yoki asabiylikning kuchayishi",
    "Hayajon bilan kurasha olmaslik",
    "Turli sabablarga ko'ra haddan tashqari tashvish",
    "Ruhiy bo'shasha olmaslik",
    "Haddan tashqari tashvish: \"o'zimga joy topolmayapman\"",
    "Xavotir yoki asabiylashish tuyg'usiga osongina taslim bo'lish",
    "Qo'rqinchli narsadan qo'rqish",
]

LEVELS: list[dict] = [
    {"min": 0, "max": 4, "label": "Minimal xavotir",
     "summary": "Xavotir darajangiz minimal — bu natija klinik ahamiyatga ega emas."},
    {"min": 5, "max": 9, "label": "Yengil xavotir",
     "summary": "Yengil darajadagi xavotir belgilari bor. Kuzatib boring, agar kuchaysa mutaxassisga murojaat qiling."},
    {"min": 10, "max": 14, "label": "O'rtacha xavotir (klinik chegara)",
     "summary": "Bu ko'rsatkich klinik skriningda \"ijobiy\" chegara hisoblanadi — psixolog yoki psixiatr bilan suhbat tavsiya etiladi."},
    {"min": 15, "max": 21, "label": "Og'ir xavotir",
     "summary": "Bu yuqori ko'rsatkich — iloji boricha tezroq psixiatr yoki psixolog bilan maslahatlashing."},
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

    return {
        "total": total,
        "min": 0,
        "max": 21,
        "level": level["label"],
        "summary": level["summary"],
        "clinicalCutoff": total >= 10,
        "source": "GAD-7 (Spitzer, Kroenke, Williams, Löwe, 2006)",
    }
