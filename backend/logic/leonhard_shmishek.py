"""
Leonhard-Shmishek xarakter aksentuatsiyasi so'rovnomasi (1970), 88 savol.

MANBA VA ISHONCHLILIK HAQIDA MUHIM IZOH:
Loyiha muallifi avval boshqa (internetdan topilgan, ehtimol AI tomonidan
qayta tuzilgan) 88-savolli versiyani taqdim etgan edi — u versiyada
multiplikatorlar to'g'ri edi, lekin savollar tartibi shubhali (10 ta
shkala bo'yicha mexanik ravishda aylanma tartibda joylashtirilgan edi,
haqiqiy standart tartibga mos kelmasdi) va matnda bir nechta aniq
buzilish (korruptsiya) bor edi. Shu sabab o'sha versiya RAD ETILDI.

O'rniga muallif asl ruscha manbani taqdim etdi:
  "тест Леонгарда Шмишека.docx" (Telegram orqali yuborilgan)
Bu fayldan 88 ta savol aynan standart (asl) tartibda, python-docx
yordamida to'g'ridan-to'g'ri chiqarib olindi va shu yerda o'zbekchaga
tarjima qilindi (matn ma'nosi saqlangan holda).

Ammo bu docx faylda BAHOLASH KALITI (qaysi savol qaysi shkalaga
tegishli, "ha"/"yo'q" yo'nalishi, multiplikatorlar) YO'Q EDI — faqat
savollar matni bor edi. Shu sabab kalit quyidagicha tiklandi:
  1. Bir nechta mustaqil manba (psycabi.net, gestalt-psy.com,
     psylab.info, golenevalada.ru va boshqalar) dan kalit qidirib
     topildi va o'zaro solishtirildi.
  2. Manbalar orasida ikkita savolda (36/39 juftligi Pedantik
     shkalasida, 74/75 juftligi Distimik/Qo'zg'aluvchan shkalalarida)
     ziddiyat topildi.
  3. Bu ziddiyatlar (a) savol matnining mazmuniy (semantik) mosligini
     tekshirish va (b) qo'shimcha qidiruv orqali hal qilindi.
  4. Yakuniy kalit 1 dan 88 gacha BARCHA raqamlarni ANIQ BIR MARTA
     qoplashi (hech qanday takror yoki bo'shliqsiz) tekshirildi — bu
     kalitning ichki izchilligini tasdiqlaydi, chunki tasodifiy yoki
     noto'g'ri kalit bunday aniq qoplashni bermaydi.
  5. Har bir shkalaning maksimal balli (savollar soni x multiplikator)
     aynan 24 ga teng ekanligi tekshirildi (bu — mashhur nashrlarda
     tasdiqlangan qat'iy qoida).

Shunga qaramay: bu hamon internetdan tiklangan kalit, muallif tomonidan
rasmiy nashr bilan bevosita solishtirilmagan. Natija sahifasida bu holat
foydalanuvchiga ochiq aytiladi (ilmiy sci-disclaimer orqali).
"""

from __future__ import annotations

QUESTIONS: list[str] = [
    "Kayfiyatingiz odatda quvnoq va g'amsizmi?",  # 1
    "Xafa bo'lishga (ranjishga) moyilmisiz?",  # 2
    "Ba'zida tez yig'lab yuborganingiz bo'lganmi?",  # 3
    "Qilayotgan ishingizda doim o'zingizni haq deb bilasizmi va bunga to'liq amin bo'lmaguningizcha tinchlanmaysizmi?",  # 4
    "O'zingizni bolalikdagiga nisbatan botirroq deb hisoblaysizmi?",  # 5
    "Kayfiyatingiz chuqur quvonchdan chuqur g'amgo'ligacha o'zgarib turadimi?",  # 6
    "Davrada (kompaniyada) e'tibor markazida bo'lasizmi?",  # 7
    "Sababsiz tund va asabiy kayfiyatda bo'lib, hech kim bilan gaplashgingiz kelmaydigan kunlaringiz bo'ladimi?",  # 8
    "Jiddiy odammisiz?",  # 9
    "Juda ilhomlanib (ruhlanib) ketishingiz mumkinmi?",  # 10
    "Tadbirkormisiz (ishbilarmonmisiz)?",  # 11
    "Kimdir sizni xafa qilsa, tezda unutasizmi?",  # 12
    "Yumshoq qalbli odammisiz?",  # 13
    "Xatni pochta qutisiga tashlagandan keyin, u tirqishda osilib qolmaganiga ishonch hosil qilish uchun qayta tekshirib ko'rasizmi?",  # 14
    "Ishda doim vijdonan harakat qilishga intilasizmi?",  # 15
    "Bolaligingizda momaqaldiroq yoki itlardan qo'rqqanmisiz?",  # 16
    "Boshqa odamlarni bir-biriga nisbatan yetarlicha talabchan emas deb hisoblaysizmi?",  # 17
    "Kayfiyatingiz hayotiy voqealar va kechinmalarga kuchli bog'liqmi?",  # 18
    "Tanishlaringiz bilan doim ochiq-dilkash (to'g'ri so'z)misiz?",  # 19
    "Kayfiyatingiz tez-tez tushkun bo'ladimi?",  # 20
    "Ilgari isterik tutqanoq yoki asab tizimi charchashi (nerv tolikishi) bo'lganmi?",  # 21
    "Kuchli ichki notinchlik yoki biror narsaga ishtiyoqli intilish holatlariga moyilmisiz?",  # 22
    "Uzoq vaqt stulda qimirlamay o'tirish sizga qiyinmi?",  # 23
    "Kimdir sizga nisbatan adolatsizlik qilsa, o'z manfaatlaringiz uchun kurashasizmi?",  # 24
    "Odamni o'ldira olarmidingiz?",  # 25
    "Qiyshiq osilgan parda yoki notekis yozilgan stol yopig'i sizni shu qadar bezovta qiladimi, hozirning o'zida to'g'rilagingiz kelib qoladimi?",  # 26
    "Bolaligingizda uyda yolg'iz qolganingizda qo'rqqanmisiz?",  # 27
    "Sababsiz tez-tez kayfiyatingiz o'zgarib turadimi?",  # 28
    "O'z ishingizga doim tirishqoqlik bilan yondashasizmi?",  # 29
    "Tez g'azablanib ketishingiz mumkinmi?",  # 30
    "Beg'amlarcha (o'ylamasdan) quvnoq bo'la olasizmi?",  # 31
    "Ba'zida quvonch hissiga butunlay berilib ketishingiz mumkinmi?",  # 32
    "Ko'ngilochar tadbirlarni o'tkazish sizga to'g'ri keladimi?",  # 33
    "Odatda odamlarga u yoki bu masalada o'z samimiy fikringizni bildirasizmi?",  # 34
    "Qon ko'rinishi sizga ta'sir qiladimi?",  # 35
    "Katta mas'uliyat talab qiladigan ish bilan mamnuniyat bilan shug'ullanasizmi?",  # 36
    "Adolatsizlikka uchragan odam uchun turib berishga moyilmisiz?",  # 37
    "Qorong'i podvalga kirish sizga qiyinmi?",  # 38
    "Mayda-chuyda (mashaqqatli) qora ishni ham sevimli ishingiz kabi sekin va puxta bajarasizmi?",  # 39
    "Ochiq (muloqotchan) odammisiz?",  # 40
    "Maktabda she'r yodlashni yaxshi ko'rarmidingiz?",  # 41
    "Bolaligingizda uydan qochib ketganmisiz?",  # 42
    "Hayotni og'ir qabul qilasizmi?",  # 43
    "Asabingizni shu qadar charchatgan janjal va noxushliklar bo'lganmi, hatto ishga chiqmay qolganmisiz?",  # 44
    "Muvaffaqiyatsizliklarda ham hazil-mutoyiba tuyg'ungizni yo'qotmaysiz, deyish mumkinmi?",  # 45
    "Kimdir sizni xafa qilsa, yarashish uchun birinchi qadamni siz qo'yasizmi?",  # 46
    "Hayvonlarni yaxshi ko'rasizmi?",  # 47
    "Ishda yoki uyda biror narsa tartibsiz bo'lsa, u yerni tark etasizmi?",  # 48
    "Siz yoki qarindoshlaringiz boshiga qandaydir baxtsizlik tushishi haqidagi noaniq fikrlar sizni qiynaydimi?",  # 49
    "Kayfiyat ob-havoga bog'liq deb hisoblaysizmi?",  # 50
    "Sahnada ko'p tomoshabin oldida chiqish qilish sizga qiyinlik tug'diradimi?",  # 51
    "Kimdir sizni ataylab qo'pollik bilan jahlingizni chiqarsa, o'zingizni yo'qotib, qo'l ko'tarib yuborishingiz mumkinmi?",  # 52
    "Ko'p muloqot qilasizmi?",  # 53
    "Biror narsadan ko'nglingiz qolsa, umidsizlikka tushib qolasizmi?",  # 54
    "Tashkilotchilik tusidagi ish sizga yoqadimi?",  # 55
    "Yo'lda ko'p to'siqlar uchrasa ham, maqsadingizga qat'iyat bilan intilasizmi?",  # 56
    "Film sizni shu qadar o'ziga tortishi mumkinki, ko'zingizga yosh keladimi?",  # 57
    "Kun bo'yi kelajagingiz yoki biror muammo haqida o'ylagan bo'lsangiz, uxlab qolish sizga qiyin bo'ladimi?",  # 58
    "Maktab yillarida sinfdoshlaringizdan ko'chirib yozish yoki ular aytib turgan javobdan foydalanishga to'g'ri kelganmi?",  # 59
    "Kechasi qabristonga borish sizga qiyinmi?",  # 60
    "Uydagi har bir narsa o'z joyida turishini katta e'tibor bilan kuzatib borasizmi?",  # 61
    "Yaxshi kayfiyatda uxlab, tushkun kayfiyatda uyg'onib, bir necha soat shu holatda qolganingiz bo'lganmi?",  # 62
    "Yangi vaziyatga osonlik bilan moslasha olasizmi?",  # 63
    "Bosh og'rig'iga moyilligingiz bormi?",  # 64
    "Tez-tez kulasizmi?",  # 65
    "Odamlarga bo'lgan haqiqiy munosabatingizni bildirmay, ular bilan iliq muomala qila olasizmi?",  # 66
    "Sizni jonli va serharakat odam deyish mumkinmi?",  # 67
    "Adolatsizlikdan qattiq azob chekasizmi?",  # 68
    "Sizni tabiatning ishtiyoqli ishqibozi deyish mumkinmi?",  # 69
    "Uxlashdan oldin yoki uydan chiqishdan oldin gaz va yorug'lik o'chirilganini, eshik yopilganini tekshirish odatingiz bormi?",  # 70
    "Qo'rqoqmisiz (tez cho'chiysizmi)?",  # 71
    "Buning uchun aniq sabab bo'lmasa ham, o'zingizni \"yettinchi osmonda\" his qilgan paytlaringiz bo'ladimi?",  # 72
    "Yoshligingizda havaskorlar to'garagi yoki teatr to'garagida ishtirok etishni yaxshi ko'rarmidingiz?",  # 73
    "Ba'zida sizni uzoqlarga tikilib qarashga (xayolga cho'mishga) chorlaydimi?",  # 74
    "Kelajakka pessimistik (umidsiz) qaraysizmi?",  # 75
    "Kayfiyatingiz qisqa vaqt ichida eng yuqori quvonchdan chuqur g'am-g'ussaga o'zgarishi mumkinmi?",  # 76
    "Do'stona davrada kayfiyatingiz osongina ko'tariladimi?",  # 77
    "G'azabni uzoq vaqt ichingizda saqlaysizmi?",  # 78
    "Boshqa odam boshiga kulfat tushsa, qattiq qayg'urasizmi?",  # 79
    "Maktabda daftar varag'iga siyoh dog'i tushsa, o'sha varaqni qayta ko'chirib yozish odatingiz bo'lganmi?",  # 80
    "Ishonuvchanlikdan ko'ra ko'proq shubhalanuvchan va ehtiyotkor deyish mumkinmi sizni?",  # 81
    "Tez-tez qo'rqinchli tush ko'rasizmi?",  # 82
    "O'z ixtiyoringizdan tashqari derazadan yoki yaqinlashib kelayotgan poezd ostiga otilish fikri xayolingizga kelganmi?",  # 83
    "Quvnoq muhitda o'zingiz ham quvonchga to'lasizmi?",  # 84
    "Og'ir (bezovta qiluvchi) masalalardan osongina chalg'ib, ular haqida o'ylamay qo'ya olasizmi?",  # 85
    "Jahlingiz chiqqanda o'zingizni tuta olishingiz qiyinmi?",  # 86
    "Ko'proq jim yurishni afzal ko'rasizmi (ha), yoki gapga ustamisiz (yo'q)?",  # 87
    "Teatr tomoshasida ishtirok etishga to'g'ri kelsa, rolga butunlay kirib, o'zingizni unutib, to'liq singib keta olarmidingiz?",  # 88
]

assert len(QUESTIONS) == 88

# Har bir shkala: nomi, ikon, tavsif, "ha"/"yo'q" bilan hisoblanadigan
# savol raqamlari (1-asosli), multiplikator.
SCALES: list[dict] = [
    {
        "key": "gipertimik", "name": "Gipertimik", "icon": "☀️",
        "desc": "Doimiy yuqori kayfiyat, faollik, tashabbuskorlik, optimizm.",
        "yes": [1, 11, 23, 33, 45, 55, 67, 77], "no": [], "mult": 3,
    },
    {
        "key": "yopishqoq", "name": "Yopishqoq (qotib qoluvchi)", "icon": "🧷",
        "desc": "Kechinmalarning uzoq davom etishi, adolat va o'ch olish hissi kuchli, shubhalanuvchan.",
        "yes": [2, 15, 24, 34, 37, 56, 68, 78, 81], "no": [12, 46, 59], "mult": 2,
    },
    {
        "key": "pedantik", "name": "Pedantik", "icon": "📐",
        "desc": "Ortiqcha puxtalik, tartib-intizomga rioya, qat'iyatsizlik, mas'uliyatdan cho'chish.",
        "yes": [4, 14, 17, 26, 39, 48, 58, 61, 70, 80, 83], "no": [36], "mult": 2,
    },
    {
        "key": "qozgaluvchan", "name": "Qo'zg'aluvchan", "icon": "⚡",
        "desc": "Impulsivlik, asabiylashuvchanlik, o'z-o'zini nazorat qilishning pasayishi.",
        "yes": [8, 20, 30, 42, 52, 64, 74, 86], "no": [], "mult": 3,
    },
    {
        "key": "distimik", "name": "Distimik", "icon": "🌧️",
        "desc": "Jiddiylik, sekin reaksiya, pessimizm, kam gapiruvchanlik.",
        "yes": [9, 21, 43, 75, 87], "no": [31, 53, 65], "mult": 3,
    },
    {
        "key": "xavotirli", "name": "Xavotirli-qo'rqinchli", "icon": "😰",
        "desc": "O'ziga ishonchsizlik, xavotirlanish, qo'rquvga moyillik.",
        "yes": [16, 27, 38, 49, 60, 71, 82], "no": [5], "mult": 3,
    },
    {
        "key": "siklotimik", "name": "Siklotimik", "icon": "🔄",
        "desc": "Kayfiyatning davriy (bir necha kun/hafta) ravishda ko'tarilib-tushib turishi.",
        "yes": [6, 18, 28, 40, 50, 62, 72, 84], "no": [], "mult": 3,
    },
    {
        "key": "demonstrativ", "name": "Demonstrativ", "icon": "🎭",
        "desc": "E'tiborni o'ziga tortishga intilish, o'zini namoyon qilish, moslashuvchanlik.",
        "yes": [7, 19, 22, 29, 41, 44, 63, 66, 73, 85, 88], "no": [51], "mult": 2,
    },
    {
        "key": "ekzaltatsiya", "name": "Ekzaltatsiyalangan", "icon": "✨",
        "desc": "His-tuyg'ularning yorqin, kuchli va tez namoyon bo'lishi (quvonch ham, g'am ham).",
        "yes": [10, 32, 54, 76], "no": [], "mult": 6,
    },
    {
        "key": "emotiv", "name": "Emotiv", "icon": "💗",
        "desc": "Nozik his-tuyg'ular, ta'sirchanlik, rahmdillik, boshqalarning holatini chuqur his qilish.",
        "yes": [3, 13, 35, 47, 57, 69, 79], "no": [25], "mult": 3,
    },
]

# Ichki izchillik tekshiruvi: har bir shkalaning savollar soni x
# multiplikatori aniq 24 bo'lishi, va 1..88 barcha raqamlar bir marta
# ishlatilishi shart (aks holda kalit noto'g'ri).
_seen: set[int] = set()
for _scale in SCALES:
    _n = len(_scale["yes"]) + len(_scale["no"])
    assert _n * _scale["mult"] == 24, f"{_scale['key']}: max ball 24 emas"
    for _q in _scale["yes"] + _scale["no"]:
        assert _q not in _seen, f"savol {_q} ikki marta ishlatilgan"
        _seen.add(_q)
assert _seen == set(range(1, 89)), "1-88 barcha savollar qoplanmagan"

BANDS = [
    (0, 12, "me'yor", "Bu xususiyat sizda yaqqol namoyon bo'lmaydi."),
    (13, 18, "moyillik", "Bu xususiyatga moyillik bor, lekin aksentuatsiya darajasida emas."),
    (19, 24, "yaqqol aksentuatsiya", "Bu xususiyat sizda kuchli va barqaror namoyon bo'ladi."),
]


def get_questions() -> list[dict]:
    options = [
        {"key": "1", "text": "Ha"},
        {"key": "0", "text": "Yo'q"},
    ]
    return [{"id": i, "prompt": q, "options": options} for i, q in enumerate(QUESTIONS)]


def _band_for(score: int) -> tuple[str, str]:
    for lo, hi, label, desc in BANDS:
        if lo <= score <= hi:
            return label, desc
    return BANDS[-1][2], BANDS[-1][3]


def calculate(answers: list[int]) -> dict:
    if len(answers) != 88:
        raise ValueError("88 ta javob kutilgan edi")
    for v in answers:
        if v not in (0, 1):
            raise ValueError(f"Noto'g'ri javob qiymati: {v}")

    # 1-asosli javob lug'ati
    ans = {i + 1: v for i, v in enumerate(answers)}

    results = []
    for scale in SCALES:
        raw = sum(1 for q in scale["yes"] if ans[q] == 1)
        raw += sum(1 for q in scale["no"] if ans[q] == 0)
        score = raw * scale["mult"]
        band, band_desc = _band_for(score)
        results.append({
            "key": scale["key"],
            "name": scale["name"],
            "icon": scale["icon"],
            "desc": scale["desc"],
            "score": score,
            "max": 24,
            "band": band,
            "bandDesc": band_desc,
        })

    results.sort(key=lambda r: r["score"], reverse=True)

    pronounced = [r for r in results if r["band"] == "yaqqol aksentuatsiya"]
    tendency = [r for r in results if r["band"] == "moyillik"]

    return {
        "results": results,
        "pronounced": pronounced,
        "tendency": tendency,
        "leading": results[0] if results else None,
    }
