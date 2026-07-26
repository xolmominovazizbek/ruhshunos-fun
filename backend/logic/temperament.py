"""Temperament (Gippokratning 4 temperamenti) — bir tanlovli test.

Manba: ruhshunos-fun.html standalone prototipidan portlangan (JS -> Python),
mazmuni o'zgarishsiz saqlangan.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Temperament:
    key: str
    label: str
    trait: str
    desc: str
    career: str
    relationship: str
    caution: str
    advice: str


TEMPERAMENTS: dict[str, Temperament] = {
    "sangvinik": Temperament(
        "sangvinik", "Sangvinik", "Faol, optimist",
        "Quvnoq, sayqal, tez moslashuvchi. Ko'p do'st bilan o'ralgan. Tez qiziqib, tez sovub qoladi.",
        "Marketing, jurnalistika, tadbirkorlik, aktyorlik",
        "Flegmatik yoki melanxolik sherik bilan yaxshi muvozanat topadi",
        "Boshlagan ishni oxiriga yetkazmaslik xavfi",
        "Bitta ishga diqqatni jamlashni mashq qiling.",
    ),
    "xolerik": Temperament(
        "xolerik", "Xolerik", "Kuchli, qaror qabul qiluvchi",
        "Yetakchi, ambitsiyali, jasur. Tez asabiylashishi mumkin. Maqsadga qaratilgan.",
        "Menejer, tadbirkor, advokat, harbiy soha",
        "Flegmatik yoki melanxolik sherik bilan yaxshi muvozanat",
        "Tezkor qaror sizni ba'zida muammoga olib kelishi mumkin",
        "Muhim qarorlarga 24 soat 'o'ylash vaqti' bering.",
    ),
    "flegmatik": Temperament(
        "flegmatik", "Flegmatik", "Sokin, barqaror",
        "Sabrli, tinch, ishonchli. Hissiyotlarni nazoratga oladi. Tez qaror qabul qilmaydi.",
        "Muhandislik, moliya, davlat xizmati, tahlilchilik",
        "Xolerik yoki sangvinik sherik bilan yaxshi muvozanat",
        "O'z fikringizni aytishdan tortinish",
        "Fikringizni ochiqroq bildirishni mashq qiling.",
    ),
    "melanxolik": Temperament(
        "melanxolik", "Melanxolik", "Sezgir, mulohazali",
        "Chuqur his etadi, ijodkor, perfeksionist. Yolg'izlikni yaxshi ko'radi. Hassos.",
        "San'at, yozuvchilik, tadqiqotchilik, psixologiya",
        "Sangvinik yoki xolerik sherik bilan yaxshi muvozanat",
        "Haddan tashqari o'z-o'zini tanqid qilish",
        "Mukammallikdan ko'ra, tugatishga ustuvorlik bering.",
    ),
}

TEMPERAMENT_QUESTIONS: list[dict] = [
    {"prompt": "Yangi guruhda birinchi marta bo'lganingizda qanday tutasiz?", "options": [
        ("sangvinik", "Tez tanish bo'ldim, hammasi bilan gaplashaman"),
        ("xolerik", "Atrofni o'rganaman, keyin to'g'ridan-to'g'ri yetakchilarni topib gaplashaman"),
        ("flegmatik", "Sokin kuzataman, keyin tabiiy ravishda gaplasha boshlayman"),
        ("melanxolik", "Bir o'zim turaman, faqat birov o'zi gaplashsa javob beraman")]},
    {"prompt": "Katta loyihani boshlashda birinchi qadamingiz qanday?", "options": [
        ("sangvinik", "Hammani jamlab, g'oyalarni birga muhokama qilaman"),
        ("xolerik", "Rejani o'zim tuzib, vazifalarni taqsimlayman"),
        ("flegmatik", "Vaqt bilan, bosqichma-bosqich harakat qilaman"),
        ("melanxolik", "Har bir detalni chuqur o'ylab, mukammal reja tuzaman")]},
    {"prompt": "Kutilmagan muammo yuzaga kelganda nima qilasiz?", "options": [
        ("sangvinik", "Hazil bilan vaziyatni yengillashtirishga harakat qilaman"),
        ("xolerik", "Darhol qaror qabul qilib, harakatga o'taman"),
        ("flegmatik", "Sabr bilan, shoshilmasdan yechim izlayman"),
        ("melanxolik", "Nima xato ketganini chuqur tahlil qilaman")]},
    {"prompt": "Do'stlar bilan dam olish rejasi tuzilganda o'zingizni qanday tutasiz?", "options": [
        ("sangvinik", "Yangi, qiziqarli joy taklif qilaman"),
        ("xolerik", "Rejani o'zim tashkil qilib, hammani boshqaraman"),
        ("flegmatik", "Ko'pchilik nima desa, o'shanga roziman"),
        ("melanxolik", "Kichik, samimiy davraga afzallik beraman")]},
    {"prompt": "Tanqidga duch kelganingizda qanday munosabatda bo'lasiz?", "options": [
        ("sangvinik", "Tez unutib, kayfiyatimni saqlab qolaman"),
        ("xolerik", "Himoyalanaman va o'z fikrimni ochiq bildiraman"),
        ("flegmatik", "Xotirjam qabul qilib, ustida o'ylayman"),
        ("melanxolik", "Uzoq vaqt yuragimga olib yuraman")]},
    {"prompt": "Ish joyida muddat (deadline) yaqinlashganda qanday harakat qilasiz?", "options": [
        ("sangvinik", "Oxirgi daqiqada energiya bilan yakunlayman"),
        ("xolerik", "Boshidanoq qat'iy jadval bo'yicha ishlayman"),
        ("flegmatik", "Bosqichma-bosqich, xotirjam davom etaman"),
        ("melanxolik", "Har bir tafsilotni tekshirib, xavotirlanaman")]},
    {"prompt": "Kimdir siz bilan rozi bo'lmasa nima qilasiz?", "options": [
        ("sangvinik", "Muloyimlik bilan mavzuni o'zgartiraman"),
        ("xolerik", "O'z fikrimni oxirigacha himoya qilaman"),
        ("flegmatik", "Bahsdan qochib, tinch yo'l izlayman"),
        ("melanxolik", "Ichimda uzoq o'ylab, keyin fikr bildiraman")]},
    {"prompt": "Bo'sh vaqtingizni qanday o'tkazishni afzal ko'rasiz?", "options": [
        ("sangvinik", "Do'stlar bilan, tashqarida, faol"),
        ("xolerik", "Foydali va samarali biror narsa bilan"),
        ("flegmatik", "Uyda, tinch va osoyishta"),
        ("melanxolik", "Yolg'iz, kitob yoki san'at bilan")]},
    {"prompt": "Jamoada ishlaganingizda rolingiz ko'proq qanday bo'ladi?", "options": [
        ("sangvinik", "Kayfiyat ko'taruvchi, muloqotchi"),
        ("xolerik", "Yetakchi, qaror qabul qiluvchi"),
        ("flegmatik", "Barqarorlik va tinchlik saqlovchi"),
        ("melanxolik", "Detallarga e'tiborli, tahlilchi")]},
    {"prompt": "Katta o'zgarish (masalan, ko'chish) ro'y berganda qanday moslashasiz?", "options": [
        ("sangvinik", "Qiziqish bilan qabul qilaman"),
        ("xolerik", "Tezda moslashib, boshqarib olaman"),
        ("flegmatik", "Sekin-asta, bosiqlik bilan moslashaman"),
        ("melanxolik", "Ancha vaqt hissiy tayyorgarlik ko'raman")]},
    {"prompt": "Xato qilib qo'yganingizda qanday munosabatda bo'lasiz?", "options": [
        ("sangvinik", "Tezda kechirim so'rab, davom etaman"),
        ("xolerik", "Xatoni tuzatishga darhol kirishaman"),
        ("flegmatik", "Vaziyatni xotirjam baholayman"),
        ("melanxolik", "O'zimni qattiq ayblab, uzoq o'ylayman")]},
    {"prompt": "Muhim qaror qabul qilishda qanday yo'l tutasiz?", "options": [
        ("sangvinik", "Ichki sezgim va hissiyotimga tayanaman"),
        ("xolerik", "Tez va qat'iy qaror qilaman"),
        ("flegmatik", "Shoshmasdan, hamma variantni o'ylayman"),
        ("melanxolik", "Har bir tafsilotni chuqur tahlil qilaman")]},
    {"prompt": "Katta olomon orasida o'zingizni qanday his qilasiz?", "options": [
        ("sangvinik", "Energiyaga to'laman, hammaga qo'shilaman"),
        ("xolerik", "Boshqaruvni o'z qo'limga olaman"),
        ("flegmatik", "Xotirjam, chetroqda kuzataman"),
        ("melanxolik", "Charchayman, tinchlikka chekinaman")]},
    {"prompt": "Sherigingiz bilan kelishmovchilik chiqsa nima qilasiz?", "options": [
        ("sangvinik", "Tezda yarashishga harakat qilaman"),
        ("xolerik", "To'g'ridan-to'g'ri muammoni ochiq muhokama qilaman"),
        ("flegmatik", "Vaqt berib, ikkalamiz ham tinchlanishini kutaman"),
        ("melanxolik", "His-tuyg'ularimni chuqur o'ylab, keyin gapiraman")]},
    {"prompt": "Yangi mahorat o'rganishda qanday yondashasiz?", "options": [
        ("sangvinik", "Qiziqarli va jonli usulni tanlayman"),
        ("xolerik", "Tezkor natija beradigan usulni tanlayman"),
        ("flegmatik", "O'z sur'atimda, shoshilmasdan o'rganaman"),
        ("melanxolik", "Nazariyani chuqur va puxta o'zlashtiraman")]},
    {"prompt": "Biror narsani tabriklash yoki nishonlashda qanday yondashasiz?", "options": [
        ("sangvinik", "Katta, quvnoq tantana uyushtiraman"),
        ("xolerik", "Aniq va tashkiliy tarzda rejalashtiraman"),
        ("flegmatik", "Sodda, tinch tarzda nishonlayman"),
        ("melanxolik", "Ma'noli, shaxsiy jestni afzal ko'raman")]},
    {"prompt": "Ish yuklamasi keskin ortib ketganda nima qilasiz?", "options": [
        ("sangvinik", "Boshqalardan yordam so'rab, kayfiyatni saqlayman"),
        ("xolerik", "Ustuvorliklarni belgilab, tezda harakat qilaman"),
        ("flegmatik", "Bosqichma-bosqich, xotirjam bajarib chiqaman"),
        ("melanxolik", "Xavotirlanib, har bir vazifani qayta-qayta tekshiraman")]},
    {"prompt": "Suhbatda gap navbati sizga kelganda odatda nima qilasiz?", "options": [
        ("sangvinik", "Qiziqarli voqealarni jonli aytib beraman"),
        ("xolerik", "Aniq va qisqa, mohiyatga o'taman"),
        ("flegmatik", "Kam gapiraman, kerak bo'lgandagina"),
        ("melanxolik", "Chuqur va mazmunli fikr bildiraman")]},
    {"prompt": "Reja kutilmaganda o'zgarib qolsa qanday munosabatda bo'lasiz?", "options": [
        ("sangvinik", "Yangi rejaga tez moslashaman"),
        ("xolerik", "Yangi rejani o'zim boshqarib olaman"),
        ("flegmatik", "Xotirjam qabul qilib, davom etaman"),
        ("melanxolik", "Bezovtalanib, avvalo tushunishga harakat qilaman")]},
    {"prompt": "Ertalabki odatlaringiz qanday boshlanadi?", "options": [
        ("sangvinik", "Musiqa yoki suhbat bilan tetiklashaman"),
        ("xolerik", "Aniq reja bo'yicha tezda ishga tushaman"),
        ("flegmatik", "Shoshilmasdan, tinch tarzda boshlayman"),
        ("melanxolik", "Jimlikda, o'z fikrlarim bilan boshlayman")]},
]


def get_questions() -> list[dict]:
    return [
        {
            "id": i,
            "prompt": q["prompt"],
            "options": [{"key": key, "text": text} for key, text in q["options"]],
        }
        for i, q in enumerate(TEMPERAMENT_QUESTIONS)
    ]


def calculate(answers: list[str]) -> dict:
    if len(answers) != len(TEMPERAMENT_QUESTIONS):
        raise ValueError(f"{len(TEMPERAMENT_QUESTIONS)} ta javob kutilgan edi, {len(answers)} ta keldi")

    scores = {key: 0 for key in TEMPERAMENTS}
    for i, answer in enumerate(answers):
        allowed = {key for key, _ in TEMPERAMENT_QUESTIONS[i]["options"]}
        if answer not in allowed:
            raise ValueError(f"{i}-savol uchun noto'g'ri javob: {answer}")
        scores[answer] += 1

    total = sum(scores.values())
    ranked = sorted(
        ({"key": k, "score": v, "pct": round(v / total * 100)} for k, v in scores.items()),
        key=lambda r: r["score"],
        reverse=True,
    )
    top = TEMPERAMENTS[ranked[0]["key"]]

    return {
        "scores": ranked,
        "dominant": {
            "key": top.key,
            "label": top.label,
            "trait": top.trait,
            "desc": top.desc,
            "career": top.career,
            "relationship": top.relationship,
            "caution": top.caution,
            "advice": top.advice,
        },
    }
