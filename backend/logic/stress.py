"""Stress darajasi — 4 ballik Likert shkalasi asosidagi test.

Manba: ruhshunos-fun.html standalone prototipidan portlangan (JS -> Python),
mazmuni o'zgarishsiz saqlangan.
"""
from __future__ import annotations

STRESS_LIKERT: list[dict] = [
    {"value": 1, "text": "Hech qachon"},
    {"value": 2, "text": "Kamdan-kam"},
    {"value": 3, "text": "Tez-tez"},
    {"value": 4, "text": "Deyarli doim"},
]

STRESS_QUESTIONS: list[str] = [
    "Kechalari uxlashga qiynalasiz yoki uyqingiz bezovta bo'ladimi?",
    "Kun davomida o'zingizni asabiy yoki tez jahli chiqadigan his qilasizmi?",
    "Boshingiz yoki mushaklaringiz (bo'yin, yelka) og'rig'idan aziyat chekasizmi?",
    "Vazifalar to'planib qolganda o'zingizni bosim ostida his qilasizmi?",
    "Diqqatingizni jamlashda qiyinchilik sezasizmi?",
    "Ovqatlanish odatlaringiz (haddan tashqari ko'p yoki kam ovqatlanish) o'zgarganmi?",
    "Kelajak haqida bezovta yoki tashvishli o'ylaringiz bo'ladimi?",
    "Dam olgandan keyin ham charchagan, energiyasiz his qilasizmi?",
    "Do'stlar yoki oila bilan uchrashishni istamay qolasizmi?",
    "Yurak urishi tezlashgan yoki nafas olish qiyinlashgan holatlarni sezasizmi?",
    "Kichik muammolar sizga katta bo'lib tuyuladimi?",
    "Ishingiz yoki o'qishingizdan zavq olish qiyinlashganmi?",
    "O'zingizni doimo shoshilayotgandek his qilasizmi?",
    "Qaror qabul qilish odatdagidan qiyinroq bo'layaptimi?",
    "Tanangizda taranglik (jag', musht qilingan qo'l va h.k.) sezasizmi?",
    "Bo'sh vaqtingiz bo'lsa ham, dam ololmayotganingizni his qilasizmi?",
    "Kayfiyatingiz tez-tez o'zgarib turadimi?",
    "O'zingizni vaziyatlarni nazorat qila olmayotgandek his qilasizmi?",
]

STRESS_LEVELS: list[dict] = [
    {"min": 18, "max": 31, "label": "Past",
     "summary": "Stress darajangiz past — hozircha his-hayajonlaringizni yaxshi boshqarayapsiz.",
     "advice": [
         "Joriy muvozanatingizni saqlash uchun muntazam dam olish va uyqu tartibiga rioya qiling",
         "Yoqimli mashg'ulotlar (sport, ijod, tabiat) uchun vaqt ajrating",
         "Yaqinlaringiz bilan sifatli vaqt o'tkazishni davom ettiring",
     ]},
    {"min": 32, "max": 45, "label": "O'rtacha",
     "summary": "O'rtacha stress darajasi — ba'zi vaziyatlar sizga bosim o'tkazmoqda, lekin buni boshqarish mumkin.",
     "advice": [
         "Kuniga 10-15 daqiqa chuqur nafas olish yoki meditatsiya mashqlarini sinab ko'ring",
         "Vazifalaringizni ustuvorlik bo'yicha tartiblang va bir vaqtning o'zida hammasini qilishga urinmang",
         "Muntazam jismoniy faollik stress gormonlarini kamaytirishga yordam beradi",
         "Uyqu va dam olish vaqtini qat'iy belgilang",
     ]},
    {"min": 46, "max": 59, "label": "Yuqori",
     "summary": "Stress darajangiz yuqori — kundalik hayotingizda charchoq va bezovtalikni sezayotgan bo'lishingiz mumkin.",
     "advice": [
         "Vaqtni boshqarish usullarini (masalan, Pomodoro) qo'llab, ishni kichik bosqichlarga bo'ling",
         "Ortiqcha majburiyatlardan voz kechishni o'rganing — hammaga \"ha\" deyish shart emas",
         "Kuniga kamida 20-30 daqiqa jismoniy mashq yoki sayr qiling",
         "Yaqin do'st yoki oila a'zosi bilan his-tuyg'ularingizni baham ko'ring",
     ]},
    {"min": 60, "max": 72, "label": "Juda yuqori",
     "summary": "Stress darajangiz juda yuqori — bu holat sog'lig'ingizga ta'sir qilishi mumkin, o'zingizga g'amxo'rlik qilish vaqti keldi.",
     "advice": [
         "Imkon qadar tezroq ish yukingizni kamaytirishga harakat qiling",
         "Nafas olish mashqlari yoki mindfulness texnikalarini kundalik odatga aylantiring",
         "Uyqu, ovqatlanish va dam olish rejimini tiklashga alohida e'tibor bering",
         "Agar holat davom etsa, professional psixolog yoki terapevt bilan maslahatlashishni ko'rib chiqing",
     ]},
]


def get_questions() -> list[dict]:
    options = [{"key": str(o["value"]), "text": o["text"]} for o in STRESS_LIKERT]
    return [{"id": i, "prompt": prompt, "options": options} for i, prompt in enumerate(STRESS_QUESTIONS)]


def _level_for(total: int) -> dict:
    for level in STRESS_LEVELS:
        if level["min"] <= total <= level["max"]:
            return level
    return STRESS_LEVELS[-1]


def calculate(answers: list[int]) -> dict:
    if len(answers) != len(STRESS_QUESTIONS):
        raise ValueError(f"{len(STRESS_QUESTIONS)} ta javob kutilgan edi, {len(answers)} ta keldi")
    for v in answers:
        if v not in {1, 2, 3, 4}:
            raise ValueError(f"Noto'g'ri javob qiymati: {v}")

    total = sum(answers)
    level = _level_for(total)

    return {
        "total": total,
        "min": 18,
        "max": 72,
        "level": level["label"],
        "summary": level["summary"],
        "advice": level["advice"],
    }
