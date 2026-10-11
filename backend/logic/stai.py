"""Spilberger-Xanin xavotirlilik so'rovnomasi (STAI, Ch.Spielberger / Yu.Xanin
rus adaptatsiyasi).

40 ta bayonot, 2 blok:
  - Blank 1 (ST, "Vaziyatli xavotirlilik") — 20 savol, hozirgi holatni so'raydi.
  - Blank 2 (LT, "Shaxsiy xavotirlilik") — 20 savol, odatdagi holatni so'raydi.

Har ikki blokda ham to'g'ridan-to'g'ri (direct) va teskari (reverse) hisoblanadigan
savollar bor. Formulasi (standart Xanin formulasi):
  ST = (to'g'ridan-to'g'ri savollar yig'indisi) - (teskari savollar yig'indisi) + 35
  LT = xuddi shunday, LT ro'yxati bo'yicha.

Bu — dunyoda eng ko'p qo'llaniladigan xavotir o'lchash vositalaridan biri,
rasmiy nashr etilgan va keng validatsiyadan o'tgan. Formuladagi savol
raqamlari va koeffitsiyentlar manbada (standart rus adaptatsiyasi)
o'zgarishsiz.
"""
from __future__ import annotations

ST_OPTIONS: list[dict] = [
    {"value": 1, "text": "Yo'q, bunday emas"},
    {"value": 2, "text": "Shunday desayam bo'ladi"},
    {"value": 3, "text": "To'g'ri"},
    {"value": 4, "text": "Mutlaqo to'g'ri"},
]

LT_OPTIONS: list[dict] = [
    {"value": 1, "text": "Hech qachon"},
    {"value": 2, "text": "Deyarli hech qachon"},
    {"value": 3, "text": "Tez-tez"},
    {"value": 4, "text": "Deyarli har doim"},
]

ST_QUESTIONS: list[str] = [
    "Men xotirjamman",
    "Menga hech narsa xavf solmayapti",
    "Men tarang holatdaman",
    "O'zimni ich-ichimdan siqilgan his qilyapman",
    "O'zimni erkin his qilyapman",
    "Men xafaman (kayfiyatim yo'q)",
    "Meni bo'lishi mumkin bo'lgan omadsizliklar tashvishlantiryapti",
    "Ruhiy xotirjamlikni his qilyapman",
    "Men xavotirdaman",
    "Ichki qoniqish hissini tuyayapman",
    "O'zimga ishonaman",
    "Men asabiylashyapman",
    "O'zimga joy topolmayapman",
    "Jizzaki bo'lib qolganman",
    "Men siqilishni va taranglikni his qilmayapman",
    "Men mamnunman",
    "Men tashvishdaman",
    "O'ta hayajondaman va o'zimni noqulay his qilyapman",
    "Men xursandman",
    "Men o'zimni yaxshi his qilayapman",
]

LT_QUESTIONS: list[str] = [
    "Menda ko'tarinki kayfiyat bo'lib turadi",
    "Men tez asabiylashib turaman",
    "Men tez xafa bo'lib qolishim mumkin",
    "Boshqalar kabi omadli bo'lishni xohlardim",
    "Ko'ngilsizliklarni qattiq qabul qilaman va ularni uzoq vaqt unuta olmayman",
    "Kuch-g'ayratga to'lganimni, ishlash istagini his qilaman",
    "Men xotirjamman, sovuqqonman va o'zimni qo'lga olganman",
    "Meni bo'lishi mumkin bo'lgan qiyinchiliklar tashvishga soladi",
    "Arzimagan narsalar (mayda-chuydalar) tufayli haddan tashqari ko'p siqilaman",
    "O'zimni baxtli his qilib turaman",
    "Hamma narsani yuragimga yaqin olaman",
    "Menga o'zimga bo'lgan ishonch yetishmaydi",
    "O'zimni himoyasiz his qilaman",
    "Keskin vaziyatlar va qiyinchiliklardan qochishga harakat qilaman",
    "Menda tushkunlik (g'amginlik) holati bo'lib turadi",
    "Men mamnun bo'lib turaman",
    "Har xil mayda-chuydalar xayolimni bo'ladi va meni xavotirga soladi",
    "Ba'zan o'zimni omadsizdek his qilaman",
    "Men bosiq odamman",
    "Ishlarim va tashvishlarim haqida o'ylaganimda meni bezovtalik qamrab oladi",
]

assert len(ST_QUESTIONS) == 20
assert len(LT_QUESTIONS) == 20

# 1-asosli savol raqamlari (har bir blok ichida)
ST_DIRECT = [3, 4, 6, 7, 9, 12, 13, 14, 17, 18]
ST_REVERSE = [1, 2, 5, 8, 10, 11, 15, 16, 19, 20]
LT_DIRECT = [2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 15, 17, 18, 20]
LT_REVERSE = [1, 6, 7, 10, 16, 19]

assert set(ST_DIRECT) | set(ST_REVERSE) == set(range(1, 21))
assert set(LT_DIRECT) | set(LT_REVERSE) == set(range(1, 21))


def _band_for(score: int) -> str:
    if score <= 30:
        return "Past"
    if score <= 44:
        return "O'rtacha"
    return "Yuqori"


def get_questions() -> list[dict]:
    st_opts = [{"key": str(o["value"]), "text": o["text"]} for o in ST_OPTIONS]
    lt_opts = [{"key": str(o["value"]), "text": o["text"]} for o in LT_OPTIONS]
    out = []
    i = 0
    for q in ST_QUESTIONS:
        out.append({"id": i, "categoryLabel": "Blank 1: Hozirgi holatingiz", "prompt": q, "options": st_opts})
        i += 1
    for q in LT_QUESTIONS:
        out.append({"id": i, "categoryLabel": "Blank 2: Odatdagi holatingiz", "prompt": q, "options": lt_opts})
        i += 1
    return out


def calculate(answers: list[int]) -> dict:
    if len(answers) != 40:
        raise ValueError("40 ta javob kutilgan edi (20 + 20)")
    for v in answers:
        if v not in (1, 2, 3, 4):
            raise ValueError(f"Noto'g'ri javob qiymati: {v}")

    st_ans = {i + 1: v for i, v in enumerate(answers[:20])}
    lt_ans = {i + 1: v for i, v in enumerate(answers[20:])}

    st = sum(st_ans[i] for i in ST_DIRECT) - sum(st_ans[i] for i in ST_REVERSE) + 35
    lt = sum(lt_ans[i] for i in LT_DIRECT) - sum(lt_ans[i] for i in LT_REVERSE) + 35

    return {
        "st": st,
        "stBand": _band_for(st),
        "lt": lt,
        "ltBand": _band_for(lt),
        "source": "STAI (Spielberger) — Yu. Xanin rus adaptatsiyasi",
    }
