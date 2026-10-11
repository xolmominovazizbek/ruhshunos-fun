"""HADS (Hospital Anxiety and Depression Scale) — Gospital xavotir va
depressiya shkalasi.

Muallif: Zigmond & Snaith (1983). Dastlab somatik (jismoniy) kasalliklar
bilan davolanayotgan bemorlarda xavotir va depressiyani baholash uchun
yaratilgan, hozir keng qo'llaniladigan standart skrining vositasi.

14 ta bayonot — 7 tasi Xavotir (A) shkalasiga, 7 tasi Depressiya (D)
shkalasiga tegishli. Har bir savolning 4 ta javob varianti bor, ularning
qiymatlari savoldan savolga farq qiladi (ba'zi savollarda "ha, doimo"
0 ball, ba'zilarida 3 ball — bu standart HADS dizaynining o'zi, items
atayin teskari (reverse) tartibda joylashtirilgan). Har bir shkala 0-21
ball, standart kesim balllari: 0-7 me'yor, 8-10 subklinik, 11-21 klinik
darajadagi aksentuatsiya.
"""
from __future__ import annotations

# Har bir element: (savol matni, [(ball, javob matni), ...])
A_ITEMS: list[tuple[str, list[tuple[int, str]]]] = [
    ("Men o'zimda taranglik, bezovtalik his qilyapman", [
        (3, "Har doim (barcha vaqt)"),
        (2, "Tez-tez"),
        (1, "Vaqt-vaqti bilan, ba'zida"),
        (0, "Umuman his qilmayman"),
    ]),
    ("Men qo'rquvni his qilyapman, xuddi qandaydir mudhish voqea sodir bo'ladigandek", [
        (3, "Shubhasiz shunday va qo'rquv juda kuchli"),
        (2, "Ha, shunday, lekin qo'rquv juda kuchli emas"),
        (1, "Ba'zida, lekin bu meni bezovta qilmaydi"),
        (0, "Umuman his qilmayman"),
    ]),
    ("Vahimali o'ylar xayolimda aylanib yuribdi", [
        (3, "Doimo"),
        (2, "Ko'p vaqt"),
        (1, "Vaqt-vaqti bilan va unchalik tez-tez emas"),
        (0, "Kamdan-kam hollarda / umuman yo'q"),
    ]),
    ("Men bemalol o'tirib, bo'shasha (erkin nafas ola) olaman", [
        (0, "Shubhasiz, shunday"),
        (1, "Shunday bo'lsa kerak"),
        (2, "Faqat kamdan-kam hollarda shunday"),
        (3, "Umuman eplay olmayapman"),
    ]),
    ("Men ichki taranglik yoki titroqni his qilyapman", [
        (0, "Umuman his qilmayman"),
        (1, "Ba'zida"),
        (2, "Tez-tez"),
        (3, "Juda tez-tez"),
    ]),
    ("Men o'zimda toqatsizlikni his qilyapman, doimo harakatda bo'lishim kerakdek", [
        (3, "Shubhasiz, shunday"),
        (2, "Shunday bo'lsa kerak"),
        (1, "Faqat qisman shunday"),
        (0, "Umuman his qilmayman"),
    ]),
    ("Menda to'satdan vahima (panika) hissi paydo bo'lib turadi", [
        (3, "Juda tez-tez"),
        (2, "Ancha tez-tez"),
        (1, "Unchalik tez-tez emas"),
        (0, "Umuman bo'lmaydi"),
    ]),
]

D_ITEMS: list[tuple[str, list[tuple[int, str]]]] = [
    ("Ilgari menga katta zavq bag'ishlagan narsalar hozir ham shunday his uyg'otmoqda", [
        (0, "Shubhasiz, shunday"),
        (1, "Shunday bo'lsa kerak"),
        (2, "Faqat juda kam darajada shunday"),
        (3, "Bu umuman noto'g'ri"),
    ]),
    ("Men kula olaman va biron voqeaning kulgili tomonini ko'ra olaman", [
        (0, "Shubhasiz, shunday"),
        (1, "Shunday bo'lsa kerak"),
        (2, "Faqat juda kam darajada shunday"),
        (3, "Umuman qila olmayman"),
    ]),
    ("Men o'zimni tetik his qilyapman", [
        (3, "Umuman his qilmayman"),
        (2, "Juda kamdan-kam hollarda"),
        (1, "Ba'zida"),
        (0, "Deyarli hamma vaqt"),
    ]),
    ("Menga hamma ishni juda sekin bajarayotgandekman tuyulyapti", [
        (3, "Deyarli hamma vaqt"),
        (2, "Tez-tez"),
        (1, "Ba'zida"),
        (0, "Umuman yo'q"),
    ]),
    ("Men tashqi ko'rinishimga e'tibor bermay qo'ydim", [
        (3, "Shubhasiz, shunday"),
        (2, "Men bunga keraklicha vaqt ajratmayapman"),
        (1, "Ehtimol, men bunga kamroq vaqt ajrata boshladim"),
        (0, "Men o'zimga avvalgidek qarayapman"),
    ]),
    ("Ishlarim (mashg'ulotlarim, qiziqishlarim) menga qoniqish hissini bera oladi deb hisoblayman", [
        (0, "Xuddi avvalgidek"),
        (1, "Ha, lekin avvalgidek darajada emas"),
        (2, "Odatdagidan ancha kamroq"),
        (3, "Umuman unday deb hisoblamayman"),
    ]),
    ("Men yaxshi kitob, radio yoki teleko'rsatuvdan zavq olaman", [
        (0, "Tez-tez"),
        (1, "Ba'zida"),
        (2, "Kamdan-kam hollarda"),
        (3, "Juda kamdan-kam / umuman yo'q"),
    ]),
]

assert len(A_ITEMS) == 7
assert len(D_ITEMS) == 7


def _band(score: int) -> tuple[str, str]:
    if score <= 7:
        return "Me'yor", "Belgilar me'yoriy chegarada."
    if score <= 10:
        return "Subklinik", "Yengil darajadagi belgilar — kuzatib boring."
    return "Klinik", "Yaqqol ifodalangan belgilar — mutaxassis ko'rigi tavsiya etiladi."


def get_questions() -> list[dict]:
    out = []
    i = 0
    for label, items in (("Xavotir (A) shkalasi", A_ITEMS), ("Depressiya (D) shkalasi", D_ITEMS)):
        for prompt, opts in items:
            options = [{"key": str(val), "text": text} for val, text in opts]
            out.append({"id": i, "categoryLabel": label, "prompt": prompt, "options": options})
            i += 1
    return out


def calculate(answers: list[int]) -> dict:
    if len(answers) != 14:
        raise ValueError("14 ta javob kutilgan edi (7 + 7)")
    for v in answers:
        if v not in (0, 1, 2, 3):
            raise ValueError(f"Noto'g'ri javob qiymati: {v}")

    score_a = sum(answers[:7])
    score_d = sum(answers[7:])
    band_a, desc_a = _band(score_a)
    band_d, desc_d = _band(score_d)

    return {
        "scoreA": score_a,
        "bandA": band_a,
        "descA": desc_a,
        "scoreD": score_d,
        "bandD": band_d,
        "descD": desc_d,
        "source": "HADS (Zigmond & Snaith, 1983)",
    }
