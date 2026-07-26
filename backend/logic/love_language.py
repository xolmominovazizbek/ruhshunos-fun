"""Sevgi tili (5 Love Languages, Gary Chapman) — A/B tanlov testi.

Manba: ruhshunos-fun.html standalone prototipidan portlangan (JS -> Python),
mazmuni o'zgarishsiz saqlangan.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LoveLanguage:
    key: str
    label: str
    short: str
    advice: str


LOVE_LANGUAGES: dict[str, LoveLanguage] = {
    "words": LoveLanguage("words", "So'z bilan ifodalash", "tilga olingan mehr va maqtovlar",
                           "Sherigingizga tez-tez minnatdorchilik va maqtov so'zlarini ayting."),
    "quality": LoveLanguage("quality", "Sifatli vaqt", "to'liq e'tibor bilan birga o'tkazilgan lahzalar",
                             "Telefonlarni yig'ishtirib, faqat bir-biringizga bag'ishlangan vaqt ajrating."),
    "gifts": LoveLanguage("gifts", "Sovg'alar", "o'ylab tanlangan kichik belgilar",
                           "Katta bo'lishi shart emas — muhimi, sizni eslab tanlanganini bilish."),
    "service": LoveLanguage("service", "Yordam", "amaliy yordam va g'amxo'rlik harakatlari",
                             "So'ramasdan turib kichik yordam ko'rsatish katta ma'no anglatadi."),
    "touch": LoveLanguage("touch", "Jismoniy yaqinlik", "quchoqlash va yaqin bo'lish",
                           "Kundalik oddiy teginish — qo'l ushlash, quchoqlash — bog'liqlikni mustahkamlaydi."),
}

LOVE_QUESTIONS: list[dict] = [
    {"prompt": "Uzoq va charchagan kundan keyin sizni eng ko'p tetiklashtiradigan narsa qaysi?", "a": ("words", "Sherigim mehr bilan gapirib, meni maqtaydi"), "b": ("quality", "Sherigim hech narsaga chalg'imay, faqat men bilan bo'ladi")},
    {"prompt": "Sevgi izhorini qanday eshitish sizga yoqadi?", "a": ("words", "Ochiq-oydin, iliq so'zlar bilan"), "b": ("gifts", "Kichik, o'ylangan sovg'alar orqali")},
    {"prompt": "Uyga charchab kelganingizda nima sizni sevilayotganingizni his qildiradi?", "a": ("words", "\"Zo'r ish qilding\" degan maqtov"), "b": ("service", "Kechki ovqat tayyor bo'lib turishi")},
    {"prompt": "Uzoqdan sog'inganingizda nima his-tuyg'ungizni qondiradi?", "a": ("words", "Iliq so'zlar bilan yozilgan xabar"), "b": ("touch", "Ko'rishganda mahkam quchoqlash")},
    {"prompt": "Sevgilingizning vaqt ajratishining qaysi shakli sizga ko'proq ta'sir qiladi?", "a": ("quality", "Telefonlarni yig'ishtirib, faqat suhbatlashish"), "b": ("gifts", "Sevgan narsamni eslab, sovg'a qilish")},
    {"prompt": "Band kunda sherigingiz sizga g'amxo'rlik qilsa, qaysi holat ko'proq yoqadi?", "a": ("quality", "Ishini to'xtatib, men bilan gaplashishi"), "b": ("service", "So'ramasdan turib uy ishlarimni bajarib qo'yishi")},
    {"prompt": "Kanapeda birga o'tirganingizda sizga nima muhimroq?", "a": ("quality", "Telefonsiz, chin dildan suhbat"), "b": ("touch", "Yonma-yon o'tirib, qo'l ushlab turish")},
    {"prompt": "Uzoq safardan qaytganida nima sizni quvontiradi?", "a": ("gifts", "Siz uchun tanlab olingan sovg'a"), "b": ("service", "Uyni tartibga keltirib qo'yishi")},
    {"prompt": "Bayramda sherigingizdan nimani kutasiz?", "a": ("gifts", "O'ylangan, ma'noli sovg'a"), "b": ("touch", "Mehr bilan quchoqlab tabriklashi")},
    {"prompt": "Kasal bo'lib qolganingizda nima eng ko'p yordam beradi?", "a": ("service", "Parvarish qilib, ovqat va dori tayyorlab berishi"), "b": ("touch", "Yonimda o'tirib, qo'limni ushlab turishi")},
    {"prompt": "Muvaffaqiyatga erishganingizda nimani ko'proq xohlaysiz?", "a": ("words", "Sherigim bu haqda faxr bilan gapirishi"), "b": ("quality", "Buni birga nishonlash uchun vaqt ajratishi")},
    {"prompt": "Uzr so'rashning qaysi usuli sizni yumshatadi?", "a": ("words", "Chin yurakdan aytilgan uzr so'zlari"), "b": ("gifts", "Kichik bir sovg'a bilan uzr so'rash")},
    {"prompt": "Sizni har kuni nima kuchli his qiladi?", "a": ("words", "\"Senga rahmat\" deb tez-tez eshitish"), "b": ("service", "Kundalik yumushlarda yordam ko'rish")},
    {"prompt": "Xafa bo'lgan paytingizda sizga nima yordam beradi?", "a": ("words", "Yupatuvchi, mehribon so'zlar"), "b": ("touch", "Jim, mehr bilan quchoqlab turish")},
    {"prompt": "Sizga eng qadrli sovg'a qaysi?", "a": ("quality", "Vaqt — ikkovimiz uchun ajratilgan kun"), "b": ("gifts", "Meni yaxshi bilgani uchun tanlangan narsa")},
    {"prompt": "Dam olish kunida sherigingizdan nimani ko'proq kutasiz?", "a": ("quality", "Butun kunni birga o'tkazishni"), "b": ("service", "Uy yumushlarida yordam berishini")},
    {"prompt": "Kino ko'rayotganingizda nimasi muhim?", "a": ("quality", "Diqqat bilan birga vaqt o'tkazish"), "b": ("touch", "Yonma-yon o'tirib, quchoqlashib turish")},
    {"prompt": "Tug'ilgan kuningizda nimani ko'proq kutasiz?", "a": ("gifts", "Diqqat bilan tanlangan sovg'ani"), "b": ("service", "Bayramni tashkil qilishda yordam berishini")},
    {"prompt": "Uzoq ish safaridan qaytganida nimani kutasiz?", "a": ("gifts", "Kichkina esdalik sovg'a"), "b": ("touch", "Eshikda kutib olib, mahkam quchoqlashini")},
    {"prompt": "Charchagan kuningizda nima sizni tinchlantiradi?", "a": ("service", "Sherigim ovqat tayyorlab, ishlarimni qilib qo'yishi"), "b": ("touch", "Yonimda o'tirib, yelkamni siypalashi")},
    {"prompt": "Munosabatingizda eng muhim narsa nima deb o'ylaysiz?", "a": ("words", "Bir-birimizga mehr so'zlarini aytib turish"), "b": ("quality", "Bir-birimizga sifatli vaqt ajratish")},
    {"prompt": "Sevgilingiz siz uchun nima qilsa, eng ko'p ta'sirlanasiz?", "a": ("quality", "Rejalarini bekor qilib, men bilan qolsa"), "b": ("gifts", "Kutilmagan sovg'a bilan hayron qoldirsa")},
    {"prompt": "Yordam kerak bo'lganida nima ko'proq ta'sir qiladi?", "a": ("gifts", "Kerakli narsani sovg'a qilib yuborishi"), "b": ("service", "Kelib, o'zi qo'lda yordam berishi")},
    {"prompt": "Bir-biringizga g'amxo'rlik qanday ko'rsatilishi kerak deb o'ylaysiz?", "a": ("service", "Amaliy ishlarda yordam berish orqali"), "b": ("touch", "Jismoniy yaqinlik va iliqlik orqali")},
    {"prompt": "Kechqurun uxlashdan oldin sizga nima yoqadi?", "a": ("touch", "Meni mahkam quchoqlab, jim uxlab qolishi"), "b": ("words", "Kunim haqida iliq so'zlar bilan xayrlashishi")},
]


def get_questions() -> list[dict]:
    return [
        {
            "id": i,
            "prompt": q["prompt"],
            "options": [
                {"key": q["a"][0], "text": q["a"][1]},
                {"key": q["b"][0], "text": q["b"][1]},
            ],
        }
        for i, q in enumerate(LOVE_QUESTIONS)
    ]


def calculate(answers: list[str]) -> dict:
    if len(answers) != len(LOVE_QUESTIONS):
        raise ValueError(f"{len(LOVE_QUESTIONS)} ta javob kutilgan edi, {len(answers)} ta keldi")

    scores = {key: 0 for key in LOVE_LANGUAGES}
    for i, answer in enumerate(answers):
        allowed = {LOVE_QUESTIONS[i]["a"][0], LOVE_QUESTIONS[i]["b"][0]}
        if answer not in allowed:
            raise ValueError(f"{i}-savol uchun noto'g'ri javob: {answer}")
        scores[answer] += 1

    total = sum(scores.values())
    ranked = sorted(
        ({"key": k, "score": v, "pct": round(v / total * 100)} for k, v in scores.items()),
        key=lambda r: r["score"],
        reverse=True,
    )
    top1, top2 = ranked[0], ranked[1]

    return {
        "scores": ranked,
        "primary": LOVE_LANGUAGES[top1["key"]].label,
        "secondary": LOVE_LANGUAGES[top2["key"]].label,
        "summary": (
            f"Sizning eng kuchli sevgi tilingiz — {LOVE_LANGUAGES[top1['key']].label} ({top1['pct']}%), "
            f"undan keyin {LOVE_LANGUAGES[top2['key']].label} ({top2['pct']}%) keladi. "
            f"Siz sevilayotganingizni ko'proq {LOVE_LANGUAGES[top1['key']].short} orqali sezasiz."
        ),
        "advice": LOVE_LANGUAGES[top1["key"]].advice,
    }
