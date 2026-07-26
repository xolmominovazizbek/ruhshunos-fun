"""Hayot soni (Life Path Number) — Pythagorean numerologiya.

Manba: @Ruhshunos_Fun loyihasi.docx, 5-bo'lim. Har bir son uchun to'liq
tavsif (kasb, munosabatlar, kuchli tomonlar, ehtiyot bo'lish kerak
bo'lgan narsa, maslahat) hujjatning 5.2/5.3-bo'limlaridagi qisqa
ta'riflar va 11-son namunasi asosida kengaytirildi.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

MASTER_NUMBERS = {11, 22, 33}


@dataclass(frozen=True)
class LifePathMeaning:
    number: int
    title: str
    summary: str
    career: str
    relationships: str
    strengths: str
    caution: str
    advice: str
    is_master: bool = False


LIFE_PATH_MEANINGS: dict[int, LifePathMeaning] = {
    1: LifePathMeaning(
        1, "Yetakchi",
        "Mustaqil, kuchli, tashabbuskor, individualist. Yetakchilikka moyil.",
        "Tadbirkor, rahbar, loyiha menejeri, harbiy yoki sport murabbiyi",
        "Mustaqil va o'ziga ishongan sherikni qadrlaydi, nazorat qilinishni yoqtirmaydi",
        "Qat'iyat, tashabbuskorlik, tez qaror qabul qilish",
        "Haddan tashqari o'jarlik va yakkaxonlikka moyillik",
        "Boshqalarning fikrini eshitishni o'rganing — yetakchilik hamkorlikni istisno qilmaydi.",
    ),
    2: LifePathMeaning(
        2, "Diplomat",
        "Sezgir, hamkorlik, muvozanat. Boshqalar bilan ishlashda kuchli.",
        "Psixolog, vositachi, HR mutaxassisi, ijtimoiy ishchi",
        "Barqaror, sodiq va uyg'un munosabatlarni izlaydi",
        "Empatiya, diplomatiya, jamoada ishlash qobiliyati",
        "Haddan tashqari boshqalarga moslashish va o'z fikrini yashirish",
        "O'z ehtiyojlaringizni ham ochiq aytishni unutmang.",
    ),
    3: LifePathMeaning(
        3, "Ijodkor",
        "Ekspressiv, optimist, ijodiy. Muloqot va san'atda iqtidorli.",
        "San'atkor, yozuvchi, dizayner, marketolog, jurnalist",
        "Quvnoq va ilhomlantiruvchi sherikni qadrlaydi",
        "Ijodkorlik, xushmuomalalik, ijobiy energiya",
        "Diqqatni jamlashda qiynalish va yuzaki munosabatga moyillik",
        "G'oyalaringizni oxirigacha yetkazishga e'tibor bering.",
    ),
    4: LifePathMeaning(
        4, "Quruvchi",
        "Mehnatkash, mas'uliyatli, ishonchli. Tartib va barqarorlikni qadrlaydi.",
        "Muhandis, moliyachi, quruvchi, menejer, tahlilchi",
        "Ishonchli va barqaror munosabatlarni afzal ko'radi",
        "Intizom, mas'uliyat, amaliy fikrlash",
        "Haddan tashqari qat'iylik va o'zgarishlardan qochish",
        "Ba'zida rejadan chetga chiqishga ham o'zingizga ruxsat bering.",
    ),
    5: LifePathMeaning(
        5, "Sayohatchi",
        "Erkin, qiziquvchan, o'zgaruvchan. Yangi tajribalarni izlaydi.",
        "Sayohat sohasi, jurnalist, savdo, startap asoschisi",
        "Erkinlikni cheklamaydigan, sarguzashtli sherikni istaydi",
        "Moslashuvchanlik, qiziquvchanlik, jasorat",
        "Barqarorlikdan qochish va qaror qabul qilishda beqarorlik",
        "Katta qarorlarda bir oz sabr qiling — har doim ham o'zgarish shart emas.",
    ),
    6: LifePathMeaning(
        6, "G'amxo'r",
        "Mehribon, oilaviy, ma'sul. Boshqalarga g'amxo'rlik qilishni yaxshi ko'radi.",
        "Shifokor, o'qituvchi, ijtimoiy soha, oila terapevti",
        "Oila va sadoqatni yuqori qo'yadi, g'amxo'r sherik izlaydi",
        "Mehr, mas'uliyat, boshqalarga yordam berish qobiliyati",
        "O'zini unutib, boshqalar uchun haddan tashqari qurbon bo'lish",
        "Boshqalarga g'amxo'rlik qilishdan oldin o'zingizga ham vaqt ajrating.",
    ),
    7: LifePathMeaning(
        7, "Mutafakkir",
        "Tahliliy, ma'naviy, izlanuvchan. Falsafa va ilmga moyil.",
        "Tadqiqotchi, olim, yozuvchi, dasturchi, ma'naviy yo'l-yo'riqchi",
        "Chuqur intellektual aloqa va shaxsiy makonni qadrlaydi",
        "Chuqur tahlil, izlanuvchanlik, ichki donolik",
        "Yolg'izlikka berilib ketish va odamlardan uzoqlashish",
        "Bilimlaringizni boshqalar bilan ulashish sizni yanada boyitadi.",
    ),
    8: LifePathMeaning(
        8, "Boshqaruvchi",
        "Ambitsiyali, moliyaviy, kuchli irodali. Biznes va karyerada muvaffaqiyatli.",
        "Biznes rahbari, investor, yurist, moliyaviy menejer",
        "Kuchli va maqsadli sherikni qadrlaydi, mustaqillikni hurmat qiladi",
        "Irodakuchi, strategik fikrlash, natijaga yo'nalganlik",
        "Ishga berilib ketib, shaxsiy hayotni e'tibordan chetda qoldirish",
        "Muvaffaqiyat faqat raqamlarda emasligini yodda tuting.",
    ),
    9: LifePathMeaning(
        9, "Insonparvar",
        "Olijanob, dunyoga ochiq, idealist. Boshqalarga yordam berishni xohlaydi.",
        "Faoliyatchi, xayriya sohasi, o'qituvchi, san'atkor, diplomat",
        "Chuqur ma'noli va insonparvar munosabatlarni izlaydi",
        "Saxiylik, keng dunyoqarash, empatiya",
        "Haddan tashqari idealizm va haqiqiy hayotdan uzoqlashish",
        "Global g'oyalar bilan bir qatorda kundalik ehtiyojlaringizni ham unutmang.",
    ),
    11: LifePathMeaning(
        11, "Master — Ilhomlantiruvchi",
        "Yuqori sezgirlik, ma'naviy yetakchilik, intuitsiya.",
        "Psixolog, muallim, san'atkor, ma'naviy yo'l-yo'riq beruvchi",
        "Sezgir va e'tiborli sherikni qidiradi",
        "Empatiya, ijodkorlik, ma'naviy chuqurlik",
        "Charchoq va o'zini qurbon qilish tendensiyasi",
        "O'z energiyangizni saqlang. Ko'p odamlarga yordam berasiz, lekin o'zingizni unutmang.",
        is_master=True,
    ),
    22: LifePathMeaning(
        22, "Master — Quruvchi-Ustoz",
        "Buyuk loyihalar, dunyo darajasidagi maqsadlar.",
        "Me'mor, yirik loyiha rahbari, ijtimoiy islohotchi, tadbirkor",
        "Katta maqsadlarni baham ko'radigan, hamfikr sherikni qadrlaydi",
        "Vizyoner fikrlash, amaliyotchilik, katta miqyosda ishlash qobiliyati",
        "Haddan tashqari yuqori talablar qo'yish va o'zini bosim ostida his qilish",
        "Katta orzularingizni kichik, amalga oshiriladigan qadamlarga bo'ling.",
        is_master=True,
    ),
    33: LifePathMeaning(
        33, "Master — Muallim",
        "Olamiy xizmat, beg'araz mehr, ma'naviy o'qituvchi.",
        "Muallim, terapevt, ma'naviy rahbar, xayriya faoliyati",
        "Beg'araz mehr va chuqur g'amxo'rlik asosidagi munosabatlarni quradi",
        "Beg'araz mehr, ilhomlantirish qobiliyati, chuqur donolik",
        "O'zini butunlay boshqalarga bag'ishlab, shaxsiy ehtiyojlarni unutish",
        "Boshqalarga xizmat qilishdan oldin o'z 'idishingizni' to'ldirib oling.",
        is_master=True,
    ),
}


def calculate_life_path(birth_date: date) -> dict:
    digits = [int(ch) for ch in birth_date.strftime("%d%m%Y")]
    total = sum(digits)
    steps = [f"{'+'.join(str(d) for d in digits)} = {total}"]

    while total > 9 and total not in MASTER_NUMBERS:
        digits = [int(ch) for ch in str(total)]
        new_total = sum(digits)
        steps.append(f"{'+'.join(str(d) for d in digits)} = {new_total}")
        total = new_total

    meaning = LIFE_PATH_MEANINGS[total]
    return {
        "number": total,
        "is_master": meaning.is_master,
        "calculation": " → ".join(steps),
        "meaning": {
            "title": meaning.title,
            "summary": meaning.summary,
            "career": meaning.career,
            "relationships": meaning.relationships,
            "strengths": meaning.strengths,
            "caution": meaning.caution,
            "advice": meaning.advice,
        },
    }
