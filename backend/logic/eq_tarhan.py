"""Emotsional intellektda o'z-o'zini baholash testi.

Muallif: Dr. Nevzat Tarhan. 33 ta bayonot, har biri 1-4 ball
(Kam/O'rtacha/Ko'p/Juda ko'p) bilan baholanadi (min=33, max=132).

Eslatma: manba hujjatdagi umumiy baholash mezonlari ("1-80 / 81-120 /
121-180 / 181 va undan yuqori") aslida boshqa test (Intellekt turlari
so'rovnomasi, 0-249 balllik shkala) uchun mo'ljallangan bo'lib, ushbu
33-132 balllik shkala uchun raqamlar mos kelmaydi (masalan, 132 dan
yuqori ball umuman olib bo'lmaydi). Loyiha muallifi bilan kelishilgan
holda mezonlar 33-132 oralig'iga mutanosib ravishda qayta hisoblandi:
bu mualliflik normasi emas, taxminiy moslashtirilgan shkala ekanligi
natija sahifasida alohida ko'rsatiladi.
"""
from __future__ import annotations

LIKERT: list[dict] = [
    {"value": 1, "text": "Kam"},
    {"value": 2, "text": "O'rtacha"},
    {"value": 3, "text": "Ko'p"},
    {"value": 4, "text": "Juda ko'p"},
]

QUESTIONS: list[str] = [
    "O'z his-tuyg'ularimni yaxshi tanib olganman.",
    "O'z his-tuyg'ularimni ifoda eta olaman.",
    "Boshqalar nima his qilayotganini bilaman.",
    "Suhbatdoshim o'z nutqi bilan nima demoqchiligini yaxshi his qilib turaman.",
    "Boshqalar men haqimda qanday fikrda ekanliklarini bilaman.",
    "O'z his-tuyg'ularimni boshqara olaman.",
    "O'zimga nisbatan qilingan tanqidlarga quloq solaman va to'g'ri xulosa chiqaraman.",
    "Ko'ngilsizliklardan keyin tezda o'zimga kela olaman.",
    "Qiyinchiliklar qarshisida pozitiv, xotirjam va ehtiyotkor bo'la olaman.",
    "O'zimni qadrlayman.",
    "O'z-o'zimni tanqid qilib turaman.",
    "O'zimni qanday xursand qilishni bilaman.",
    "Har qanday qiyin vaziyatlardan chiqib keta olaman.",
    "Butun e'tiborimni muammolarga qarata olaman.",
    "Menga bosim o'tkazilganda o'zimni qanday tutishni bilaman.",
    "Muammoga duch kelsam, dardimni bo'lisha oladigan kishilarim bor.",
    "Atrofimda muammoga duch kelsa, dardini men bilan baham ko'radigan kishilar bor.",
    "Qiyinchiliklarga duch kelganda osonlikcha taslim bo'lmayman.",
    "Atrofimdagi insonlarga ishonaman.",
    "O'z hayotiy maqsadlarimga egaman.",
    "Har doim o'zim uchun zaxira maqsadlarni belgilab olaman.",
    "Maqsadimga erishish uchun turli variantlarni ishlab chiqaman.",
    "Ishonchim komilki, maqsadimga erishaman.",
    "Hayotimni boshqarish o'z qo'limda ekanligiga ishonaman.",
    "Ichki xotirjamlikka egaman deb ayta olaman.",
    "O'zim haqimda maqtov eshitganda, o'zimni yo'qotib qo'ymayman.",
    "Atrofdagilarga bepisand munosabatda bo'lmayman.",
    "O'z xatti-harakatlarimni hisob qilib turaman.",
    "Haqiqat bilan yuzlashishdan qochmayman.",
    "Qo'rquvlarimni nazorat qila olaman.",
    "Kelajakdagi hayotimni real baholay olaman.",
    "O'zim bilan o'zim kelisha olaman.",
    "Odatda pozitiv kayfiyatda yuraman, deyarli tushkunlikka tushmayman.",
]

LEVELS: list[dict] = [
    {"min": 33, "max": 65, "label": "Qoniqarsiz",
     "summary": "Hozircha hissiy intellekt ko'nikmalaringiz rivojlanish bosqichida — bu tuzatib bo'lmaydigan holat emas, mashq bilan yaxshilanadi.",
     "advice": [
         "His-tuyg'ularingizni kundalikda yozib borish o'z-o'zini anglashni kuchaytiradi",
         "Stressli vaziyatlarda darhol reaksiya bermasdan, bir necha soniya to'xtab o'ylang",
         "Ishonchli do'st yoki mutaxassis bilan muntazam suhbatlashish foydali bo'ladi",
     ]},
    {"min": 66, "max": 81, "label": "O'rtacha",
     "summary": "Hissiy intellektingiz o'rtacha darajada — ba'zi ko'nikmalaringiz kuchli, ba'zilari rivojlanishga muhtoj.",
     "advice": [
         "Eng past baho olgan savollaringizga alohida e'tibor qarating",
         "Maqsad qo'yish va rejalashtirish ko'nikmalarini mashq qiling",
         "Qiyinchiliklarda tez taslim bo'lmaslikni mashq sifatida ko'ring",
     ]},
    {"min": 82, "max": 105, "label": "Baland",
     "summary": "Hissiy intellektingiz yaxshi darajada — o'zingizni va atrofdagilarni anglash, qiyinchiliklarga bardosh berish qobiliyatingiz kuchli.",
     "advice": [
         "Kuchli tomonlaringizni boshqalarga yordam berishda ishlating",
         "O'zingizga qo'ygan maqsadlaringizni yozma tarzda kuzatib boring",
         "Muvozanatingizni saqlash uchun dam olishni ham unutmang",
     ]},
    {"min": 106, "max": 132, "label": "Juda baland",
     "summary": "Hissiy intellektingiz yuqori darajada — o'z-o'zini anglash, hissiyotlarni boshqarish va qiyinchiliklarga bardoshlilik kuchli rivojlangan.",
     "advice": [
         "Bu kuchli tomoningizni yetakchilik yoki mentorlik vazifalarida qo'llang",
         "Boshqalarga ham hissiy barqarorlikni o'rgatishda yordam bering",
         "O'zingizni g'amxo'rlik qilishni ham unutmang — doim kuchli bo'lish shart emas",
     ]},
]


def get_questions() -> list[dict]:
    options = [{"key": str(o["value"]), "text": o["text"]} for o in LIKERT]
    return [{"id": i, "prompt": q, "options": options} for i, q in enumerate(QUESTIONS)]


def _level_for(total: int) -> dict:
    for level in LEVELS:
        if level["min"] <= total <= level["max"]:
            return level
    return LEVELS[-1] if total > LEVELS[-1]["max"] else LEVELS[0]


def calculate(answers: list[int]) -> dict:
    if len(answers) != len(QUESTIONS):
        raise ValueError(f"{len(QUESTIONS)} ta javob kutilgan edi, {len(answers)} ta keldi")
    for v in answers:
        if v not in {1, 2, 3, 4}:
            raise ValueError(f"Noto'g'ri javob qiymati: {v}")

    total = sum(answers)
    level = _level_for(total)

    return {
        "total": total,
        "min": 33,
        "max": 132,
        "level": level["label"],
        "summary": level["summary"],
        "advice": level["advice"],
        "author": "Dr. Nevzat Tarhan",
        "scale_note": (
            "Umumiy baholash mezonlari asl manbadagi boshqa test shkalasidan "
            "33-132 balllik oraliqqa mutanosib moslashtirilgan taxminiy "
            "ko'rsatkich — muallifning rasmiy normasi emas."
        ),
    }
