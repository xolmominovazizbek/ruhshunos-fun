"""Zodiak belgisi aniqlash va juftlik moslik hisoblash.

Manba: @Ruhshunos_Fun loyihasi.docx, 4-bo'lim.

Hujjatdagi moslik matritsalari to'liq emas edi (ba'zi element/masofa
juftliklari uchun foiz berilmagan). Quyidagi taxminlar shu bo'shliqlarni
to'ldirish uchun qo'shildi va aniq raqamlar berilsa oson almashtiriladi:
- Element: Olov+Tuproq va Havo+Suv = 55% (hujjatda yo'q, neytral qiymat)
- Modallik: faqat 3 toifa bo'lgani uchun "bir xil" (80%) / "har xil" (90%)
  ikki holatga soddalashtirildi ("qarama-qarshi" tushunchasi doc'da 3 toifali
  tizimda mantiqan aniq emas edi)
- Masofa: 30° (1 belgi farq) = 75%, 150° (5 belgi farq) = 55% (doc'da yo'q,
  qo'shni qiymatlar orasida taxminiy interpolatsiya)
- Jins koeffitsienti: ikkala jins kiritilib har xil bo'lsa = 85%,
  aks holda (bir xil/kiritilmagan) = 70%
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ZodiacSign:
    key: str
    name: str
    emoji: str
    element: str
    element_emoji: str
    modality: str
    date_range: str
    description: str


# Zodiak g'ildiragi tartibida (0° dan boshlab), doc 4.2-bo'limi
ZODIAC_SIGNS: list[ZodiacSign] = [
    ZodiacSign(
        "hamal", "Hamal (Qo'chqor)", "♈", "Olov", "\U0001F525", "Kardinal",
        "21 mart – 19 aprel",
        "Hamal tug'ilganlar tashabbuskor, jasur va mustaqil bo'lishadi. "
        "Ular yangi ishlarni boshlashni yaxshi ko'radi, tez qaror qabul qiladi "
        "va yetakchilikka moyil. Sabr-toqat ularning zaif tomoni bo'lishi mumkin.",
    ),
    ZodiacSign(
        "savr", "Savr (Buqa)", "♉", "Tuproq", "\U0001F30D", "Sobit",
        "20 aprel – 20 may",
        "Savr vakillari barqaror, ishonchli va qat'iyatli. Ular qulaylik va "
        "farovonlikni qadrlashadi, o'zgarishlarga sekin moslashadi, lekin "
        "boshlagan ishini oxiriga yetkazishda tengsiz.",
    ),
    ZodiacSign(
        "javzo", "Javzo (Egizaklar)", "♊", "Havo", "\U0001F4A8", "Mutable",
        "21 may – 20 iyun",
        "Javzo tug'ilganlar qiziquvchan, tez fikrlaydigan va muloqotga usta. "
        "Ular ko'p qirrali bo'lib, doim yangi g'oyalar va mavzular izlaydi, "
        "ammo bir joyda uzoq to'xtab qolishni yoqtirmaydi.",
    ),
    ZodiacSign(
        "saraton", "Saraton (Qisqichbaqa)", "♋", "Suv", "\U0001F4A7", "Kardinal",
        "21 iyun – 22 iyul",
        "Saraton vakillari juda sezgir, g'amxo'r va oilaviy qadriyatlarga "
        "sodiq. Ular yaqinlarini himoya qilishga tayyor, kayfiyati tez "
        "o'zgarishi mumkin, lekin his-tuyg'ulari chuqur va samimiy.",
    ),
    ZodiacSign(
        "asad", "Asad (Sher)", "♌", "Olov", "\U0001F525", "Sobit",
        "23 iyul – 22 avgust",
        "Asad tug'ilganlar o'ziga ishongan, saxiy va tabiiy yetakchi. Ular "
        "e'tibor markazida bo'lishni yaxshi ko'rishadi, ijodiy energiyaga "
        "boy, lekin ba'zan haddan tashqari mag'rur bo'lib qolishi mumkin.",
    ),
    ZodiacSign(
        "sunbula", "Sunbula (Boshoqcha)", "♍", "Tuproq", "\U0001F30D", "Mutable",
        "23 avgust – 22 sentyabr",
        "Sunbula vakillari puxta, tahliliy va mukammallikka intiluvchan. "
        "Ular detallarga e'tiborli, mas'uliyatli va foydali bo'lishni "
        "istaydi, ammo o'zlariga va boshqalarga nisbatan juda talabchor.",
    ),
    ZodiacSign(
        "mezon", "Mezon (Tarozi)", "♎", "Havo", "\U0001F4A8", "Kardinal",
        "23 sentyabr – 22 oktyabr",
        "Mezon tug'ilganlar muvozanat, adolat va uyg'unlikni qadrlashadi. "
        "Ular diplomatik, jamoaviy ishlarda kuchli, lekin qaror qabul "
        "qilishda ikkilanib qolishlari mumkin.",
    ),
    ZodiacSign(
        "aqrab", "Aqrab (Chayon)", "♏", "Suv", "\U0001F4A7", "Sobit",
        "23 oktyabr – 21 noyabr",
        "Aqrab vakillari kuchli irodali, sirli va chuqur his qiluvchi "
        "insonlar. Ular sodiqlikni va haqiqatni qadrlashadi, ishtiyoqli "
        "va qat'iyatli, lekin ba'zan shubhali bo'lib qolishlari mumkin.",
    ),
    ZodiacSign(
        "qavs", "Qavs (O'qchi)", "♐", "Olov", "\U0001F525", "Mutable",
        "22 noyabr – 21 dekabr",
        "Qavs tug'ilganlar erkinlikni sevuvchi, optimist va sarguzashtga "
        "moyil. Ular falsafa va sayohatga qiziqishadi, ochiq fikrli, lekin "
        "ba'zan haddan tashqari to'g'riso'z bo'lishi mumkin.",
    ),
    ZodiacSign(
        "jadi", "Jadi (Tog' echkisi)", "♑", "Tuproq", "\U0001F30D", "Kardinal",
        "22 dekabr – 19 yanvar",
        "Jadi vakillari intizomli, mas'uliyatli va maqsadga yo'naltirilgan. "
        "Ular sabr bilan cho'qqilarni zabt etishadi, amaliy fikrlaydi, "
        "lekin ba'zan haddan tashqari jiddiy bo'lib qolishlari mumkin.",
    ),
    ZodiacSign(
        "dalv", "Dalv (Ko'za)", "♒", "Havo", "\U0001F4A8", "Sobit",
        "20 yanvar – 18 fevral",
        "Dalv tug'ilganlar mustaqil fikrli, innovatsion va insonparvar. "
        "Ular jamiyat manfaati uchun g'oyalar bilan chiqishadi, o'ziga xos "
        "bo'lishni yaxshi ko'radi, lekin his-tuyg'ularini yashirishi mumkin.",
    ),
    ZodiacSign(
        "hut", "Hut (Baliq)", "♓", "Suv", "\U0001F4A7", "Mutable",
        "19 fevral – 20 mart",
        "Hut vakillari xayolparast, mehribon va yuqori sezgirlikka ega. "
        "Ular san'at va ma'naviyatga moyil, boshqalarga chuqur hamdard "
        "bo'ladi, lekin real hayotdan uzoqlashib qolishlari mumkin.",
    ),
]

_SIGN_BY_KEY = {s.key: s for s in ZODIAC_SIGNS}

# (oy, kun) chegarasi -> belgi indeksi. Har bir belgi "boshlanish sanasi"dan
# navbatdagi belgi boshlanishigacha davom etadi.
_START_DATES = [
    (3, 21), (4, 20), (5, 21), (6, 21), (7, 23), (8, 23),
    (9, 23), (10, 23), (11, 22), (12, 22), (1, 20), (2, 19),
]


def get_sign_for_date(month: int, day: int) -> ZodiacSign:
    for i, (start_month, start_day) in enumerate(_START_DATES):
        next_month, next_day = _START_DATES[(i + 1) % 12]
        if start_month <= 12 and next_month < start_month:
            # yil oxiridan boshlanib, keyingi yilga o'tadigan oraliq (Jadi: 22-dek - 19-yan)
            in_range = (month, day) >= (start_month, start_day) or (month, day) < (next_month, next_day)
        else:
            in_range = (start_month, start_day) <= (month, day) < (next_month, next_day)
        if in_range:
            return ZODIAC_SIGNS[i]
    raise ValueError("Sana uchun zodiak belgisi topilmadi")


def get_sign(birth_date: date) -> ZodiacSign:
    return get_sign_for_date(birth_date.month, birth_date.day)


def get_sign_by_key(key: str) -> ZodiacSign:
    if key not in _SIGN_BY_KEY:
        raise ValueError(f"Noma'lum zodiak belgisi: {key}")
    return _SIGN_BY_KEY[key]


_ELEMENT_SCORES = {
    frozenset(["Olov"]): 95,
    frozenset(["Tuproq"]): 90,
    frozenset(["Havo"]): 85,
    frozenset(["Suv"]): 92,
    frozenset(["Olov", "Havo"]): 80,
    frozenset(["Tuproq", "Suv"]): 78,
    frozenset(["Olov", "Suv"]): 45,
    frozenset(["Tuproq", "Havo"]): 50,
    frozenset(["Olov", "Tuproq"]): 55,
    frozenset(["Havo", "Suv"]): 55,
}

_DISTANCE_SCORES = {0: 70, 1: 75, 2: 90, 3: 40, 4: 95, 5: 55, 6: 65}


def _element_score(a: ZodiacSign, b: ZodiacSign) -> int:
    return _ELEMENT_SCORES[frozenset([a.element, b.element])]


def _modality_score(a: ZodiacSign, b: ZodiacSign) -> int:
    return 80 if a.modality == b.modality else 90


def _distance_score(a: ZodiacSign, b: ZodiacSign) -> int:
    idx_a = ZODIAC_SIGNS.index(a)
    idx_b = ZODIAC_SIGNS.index(b)
    raw = abs(idx_a - idx_b)
    distance = min(raw, 12 - raw)  # 0..6 oralig'iga tushirish
    return _DISTANCE_SCORES[distance]


def _gender_score(gender_a: str | None, gender_b: str | None) -> int:
    if gender_a and gender_b and gender_a != gender_b:
        return 85
    return 70


def compatibility(
    sign_a: ZodiacSign,
    sign_b: ZodiacSign,
    gender_a: str | None = None,
    gender_b: str | None = None,
) -> dict:
    element = _element_score(sign_a, sign_b)
    modality = _modality_score(sign_a, sign_b)
    distance = _distance_score(sign_a, sign_b)
    gender = _gender_score(gender_a, gender_b)

    total = round(element * 0.4 + modality * 0.3 + distance * 0.2 + gender * 0.1)

    if total >= 85:
        energy = "Juda yuqori"
        summary = "Bu ajoyib moslik! Ikkovingiz bir-biringizni tabiiy ravishda to'ldirasiz."
    elif total >= 70:
        energy = "Yuqori"
        summary = "Yaxshi moslik. Kichik farqlar bo'lsa ham, umumiy uyg'unlik kuchli."
    elif total >= 55:
        energy = "O'rtacha"
        summary = "O'rtacha moslik — muvaffaqiyat uchun ikkovingiz ham harakat qilishingiz kerak."
    else:
        energy = "Past"
        summary = "Bu murakkab moslik. Farqlaringiz ko'p, lekin ular ham o'sish imkoniyati bo'lishi mumkin."

    if sign_a.element == sign_b.element:
        element_note = f"{sign_a.element} + {sign_a.element} — bir xil energiya, kuchli rezonans"
    else:
        element_note = f"{sign_a.element} + {sign_b.element} — turli energiyalar"

    problems = []
    if sign_a.modality == sign_b.modality == "Kardinal":
        problems.append("Ikkalangiz ham yetakchi bo'lishni xohlaysiz")
    elif sign_a.modality == sign_b.modality == "Sobit":
        problems.append("Ikkalangiz ham qarorlaringizdan qaytmasligingiz mumkin")
    elif sign_a.modality == sign_b.modality == "Mutable":
        problems.append("Ikkalangiz ham qat'iy qaror qabul qilishda qiynalishingiz mumkin")
    if element in (45, 50, 55):
        problems.append("Elementlaringiz farqli — bir-biringizni tushunish uchun ko'proq vaqt kerak bo'ladi")
    if not problems:
        problems.append("Jiddiy nomuvofiqlik kuzatilmadi, lekin har qanday munosabat mehnat talab qiladi")

    advice = (
        "Bir-biringizga gap berish va farqlaringizni qadrlashni o'rganing. "
        "Ochiq muloqot har qanday moslikni yanada mustahkamlaydi."
    )

    return {
        "total": total,
        "energy": energy,
        "summary": summary,
        "element_note": element_note,
        "communication": "Ochiq va to'g'ridan-to'g'ri" if element >= 80 else "Sabr va tushunish talab qiladi",
        "problems": problems,
        "advice": advice,
        "breakdown": {
            "element": element,
            "modality": modality,
            "distance": distance,
            "gender": gender,
        },
    }
