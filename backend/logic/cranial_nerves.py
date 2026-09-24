"""
Bosh miya nervlari (I, II, III, IV, VI juftlar) — bilim testi.

Manba: foydalanuvchi taqdim etgan "bosh_miya_nervlari_telegram.py" faylidagi
50 ta savol-javob-izoh to'plami (Telegram viktorina uchun tuzilgan edi, shu
matn o'zgarishsiz ko'chirib olindi). Bu psixologik o'z-o'zini baholash testi
EMAS — bu neyroanatomiya bo'yicha ob'ektiv bilim testi (har bir savolda bitta
to'g'ri javob bor). Shu sabab u saytning "Tibbiy bilim testlari" bo'limiga
joylashtiriladi, "ilmiy asoslangan" psixologik testlar qatoriga emas.
"""

from __future__ import annotations

import json
import random

_RAW = json.loads(r'''[
 {
  "mavzu": "I juft",
  "savol": "Hid bilish yo'lining birinchi neyronlari qayerda joylashgan?",
  "javoblar": [
   "Burun bo'shlig'i shilliq qavatining hid bilish sohasida (regio olfactoria)",
   "Hid bilish piyozchasida (bulbus olfactorius)",
   "Hid bilish uchburchagida",
   "Parahippokampal pushtada"
  ],
  "izoh": "Birinchi neyronlar — burun shilliq qavatining yuqori qismidagi bipolyar hid bilish hujayralari. Ularning aksonlari hid bilish iplarini (fila olfactoria) hosil qiladi."
 },
 {
  "mavzu": "I juft",
  "savol": "Hid bilish iplari kalla bo'shlig'iga qaysi tuzilma orqali o'tadi?",
  "javoblar": [
   "G'alvirsimon suyakning teshikli plastinkasi (lamina cribrosa)",
   "Yuqori ko'z yorig'i",
   "Ko'ruv kanali",
   "Yumaloq teshik"
  ],
  "izoh": "Fila olfactoria lamina cribrosa teshiklaridan o'tib, hid bilish piyozchasiga boradi. Shu sababli oldingi kalla chuqurchasi sinishida anosmiya ko'p uchraydi."
 },
 {
  "mavzu": "I juft",
  "savol": "Hid bilish yo'lining ikkinchi neyronlari (mitral hujayralar) qayerda joylashgan?",
  "javoblar": [
   "Hid bilish piyozchasida",
   "Burun shilliq qavatida",
   "Talamusda",
   "Ilgaksimon qismda (uncus)"
  ],
  "izoh": "Mitral hujayralar bulbus olfactorius'da joylashgan; ularning aksonlari hid bilish yo'lini (tractus olfactorius) hosil qiladi."
 },
 {
  "mavzu": "I juft",
  "savol": "Hid bilish analizatorining po'stloq markazi qayerda joylashgan?",
  "javoblar": [
   "Parahippokampal pushta va ilgaksimon qism (uncus) sohasida",
   "Ensa bo'lagi shporasimon egati atrofida",
   "Geshlning ko'ndalang pushtalarida",
   "Markaziy orqa pushtada"
  ],
  "izoh": "Hid bilishning oliy markazi chakka bo'lagining medial yuzasida — gyrus parahippocampalis va uncus sohasida joylashgan."
 },
 {
  "mavzu": "I juft",
  "savol": "Hid bilishning to'liq yo'qolishi qanday ataladi?",
  "javoblar": [
   "Anosmiya",
   "Giposmiya",
   "Parosmiya",
   "Giperosmiya"
  ],
  "izoh": "Anosmiya — hid bilishning to'liq yo'qolishi; giposmiya — pasayishi; parosmiya — hidlarni noto'g'ri qabul qilish; giperosmiya — o'tkirlashishi."
 },
 {
  "mavzu": "I juft",
  "savol": "Hid bilish gallyutsinatsiyalari (unsinat tutqanoqlar) qaysi soha shikastlanishiga xos?",
  "javoblar": [
   "Chakka bo'lagining medial qismi (uncus)",
   "Hid bilish piyozchasi",
   "Peshona bo'lagining konveksital yuzasi",
   "Ensa bo'lagi"
  ],
  "izoh": "Po'stloq markazi (uncus) ta'sirlanganda hid bilish gallyutsinatsiyalari yoki unsinat tutqanoqlar paydo bo'ladi. Periferik qism shikastlanishi esa anosmiya/giposmiya beradi."
 },
 {
  "mavzu": "I juft",
  "savol": "Hid bilish yo'lining boshqa sezgi yo'llaridan asosiy farqi nimada?",
  "javoblar": [
   "Talamusda kalit almashmasdan bevosita po'stloqqa boradi",
   "Faqat qarama-qarshi yarim sharga boradi",
   "Uch neyronli emas, ikki neyronli yo'l",
   "Miya stvolida kesishadi"
  ],
  "izoh": "Hid bilish — talamusni chetlab o'tib, to'g'ridan-to'g'ri qadimgi po'stloqqa (paleokorteks) boradigan yagona sezgi turi."
 },
 {
  "mavzu": "I juft",
  "savol": "Hid bilishni tekshirishda qaysi modda ishlatilmaydi?",
  "javoblar": [
   "Nashatir spirti (ammiak)",
   "Kofe",
   "Sovun",
   "Valeriana damlamasi"
  ],
  "izoh": "Ammiak, sirka kabi o'tkir moddalar uch shoxli nerv oxirlarini ta'sirlaydi, shuning uchun anosmiyada ham his qilinadi va natijani buzadi."
 },
 {
  "mavzu": "I juft",
  "savol": "Bir tomonlama anosmiya, shu tomonda ko'ruv nervi atrofiyasi va qarama-qarshi tomonda ko'ruv nervi diski dimlanishi qanday ataladi?",
  "javoblar": [
   "Foster-Kennedi sindromi",
   "Argayll-Robertson sindromi",
   "Veber sindromi",
   "Bernar-Horner sindromi"
  ],
  "izoh": "Foster-Kennedi sindromi peshona bo'lagining asosi yoki hid bilish chuqurchasi o'smalarida (ko'pincha meningioma) kuzatiladi."
 },
 {
  "mavzu": "II juft",
  "savol": "Ko'ruv nervini qaysi hujayralarning aksonlari hosil qiladi?",
  "javoblar": [
   "To'r pardaning ganglioz hujayralari",
   "Tayoqcha va kolbachalar",
   "Bipolyar hujayralar",
   "Lateral tizzasimon tana hujayralari"
  ],
  "izoh": "Ko'ruv yo'li: fotoretseptorlar → bipolyar hujayralar → ganglioz hujayralar. Ganglioz hujayralar aksonlari ko'ruv nervini tashkil qiladi."
 },
 {
  "mavzu": "II juft",
  "savol": "Ko'ruv nervi ko'z kosasidan kalla bo'shlig'iga qaysi teshik orqali kiradi?",
  "javoblar": [
   "Ko'ruv kanali (canalis opticus)",
   "Yuqori ko'z yorig'i",
   "Pastki ko'z yorig'i",
   "Oval teshik"
  ],
  "izoh": "N. opticus ko'z arteriyasi (a. ophthalmica) bilan birga canalis opticus orqali o'tadi."
 },
 {
  "mavzu": "II juft",
  "savol": "Ko'ruv kesishmasida (chiasma opticum) qaysi tolalar kesishadi?",
  "javoblar": [
   "To'r pardaning medial (burun) yarmidan keluvchi tolalar",
   "To'r pardaning lateral (chakka) yarmidan keluvchi tolalar",
   "Barcha tolalar",
   "Faqat makulyar tolalar"
  ],
  "izoh": "Burun yarmidan kelgan tolalar kesishadi, chakka yarmidagilar o'z tomonida qoladi. Shuning uchun har bir ko'ruv trakti ikkala ko'zning bir nomli yarmlaridan tola olib boradi."
 },
 {
  "mavzu": "II juft",
  "savol": "Gipofiz adenomasi xiazmaning markaziy qismini ezganda qanday ko'ruv maydoni buzilishi kuzatiladi?",
  "javoblar": [
   "Bitemporal gemianopsiya",
   "Binazal gemianopsiya",
   "Gomonim gemianopsiya",
   "Bir ko'zda amavroz"
  ],
  "izoh": "Kesishuvchi burun tolalari shikastlanadi — ikkala ko'zda chakka (tashqi) ko'ruv maydonlari tushib qoladi: heteronim bitemporal gemianopsiya."
 },
 {
  "mavzu": "II juft",
  "savol": "Xiazmaning ikkala lateral qismi (masalan, ichki uyqu arteriyalarining ikki tomonlama sklerozi yoki anevrizmasida) ezilsa nima kuzatiladi?",
  "javoblar": [
   "Binazal gemianopsiya",
   "Bitemporal gemianopsiya",
   "Qarama-qarshi gomonim gemianopsiya",
   "Yuqori kvadrant gemianopsiyasi"
  ],
  "izoh": "Lateral qismlarda kesishmagan chakka tolalari o'tadi; ular shikastlanganda ichki (burun) ko'ruv maydonlari tushadi."
 },
 {
  "mavzu": "II juft",
  "savol": "Chap ko'ruv trakti shikastlanganda qanday buzilish kuzatiladi?",
  "javoblar": [
   "O'ng tomonlama gomonim gemianopsiya",
   "Chap tomonlama gomonim gemianopsiya",
   "Bitemporal gemianopsiya",
   "Chap ko'zda amavroz"
  ],
  "izoh": "Trakt ikkala ko'zning bir nomli yarmlaridan tola olib boradi — shikastlanganda qarama-qarshi tomondagi ko'ruv maydonlari tushadi (kontralateral gomonim gemianopsiya)."
 },
 {
  "mavzu": "II juft",
  "savol": "Qaysi tuzilma birlamchi (po'stloq osti) ko'ruv markazi hisoblanadi?",
  "javoblar": [
   "Lateral tizzasimon tana",
   "Medial tizzasimon tana",
   "To'rt tepalikning pastki tepaliklari",
   "Qizil yadro"
  ],
  "izoh": "Po'stloq osti ko'ruv markazlari: lateral tizzasimon tana, talamus yostiqchasi (pulvinar) va yuqori tepaliklar. Medial tizzasimon tana va pastki tepaliklar — eshituv markazlari."
 },
 {
  "mavzu": "II juft",
  "savol": "Ko'ruv analizatorining po'stloq markazi qayerda joylashgan?",
  "javoblar": [
   "Ensa bo'lagidagi shporasimon egat (sulcus calcarinus) atrofida",
   "Chakka bo'lagining yuqori pushtasida",
   "Peshona bo'lagining o'rta pushtasida",
   "Burchakli pushtada"
  ],
  "izoh": "Birlamchi ko'ruv po'stlog'i — Brodmanning 17-maydoni, sulcus calcarinus'ning ikki labida (ponasimon qism va tilsimon pushta)."
 },
 {
  "mavzu": "II juft",
  "savol": "Chakka bo'lagidagi ko'ruv nurlanishi (Graziole tutami, Meyer halqasi) shikastlanganda qanday buzilish kuzatiladi?",
  "javoblar": [
   "Qarama-qarshi tomonda yuqori kvadrant gemianopsiyasi",
   "Qarama-qarshi tomonda pastki kvadrant gemianopsiyasi",
   "Bitemporal gemianopsiya",
   "Shu tomonda amavroz"
  ],
  "izoh": "Chakka bo'lagidan to'r pardaning pastki qismlaridan kelgan tolalar o'tadi, ular ko'ruv maydonining yuqori kvadrantlariga mos keladi."
 },
 {
  "mavzu": "II juft",
  "savol": "Qarama-qarshi gomonim gemianopsiya bo'lib, markaziy (makulyar) ko'rish saqlangan bo'lsa, shikastlanish qayerda?",
  "javoblar": [
   "Ensa bo'lagi po'stlog'ida (shporasimon egat)",
   "Ko'ruv traktida",
   "Xiazmada",
   "Ko'ruv nervida"
  ],
  "izoh": "Makulaning po'stloqdagi vakilligi keng va ikki tomonlama qon bilan ta'minlanadi, shuning uchun ensa po'stlog'i shikastlanganda markaziy ko'rish ko'pincha saqlanadi."
 },
 {
  "mavzu": "II juft",
  "savol": "Ko'z tubida ko'ruv nervi diskining dimlanishi ko'pincha nimadan dalolat beradi?",
  "javoblar": [
   "Kalla ichi bosimining oshishidan",
   "Ko'ruv nervining birlamchi atrofiyasidan",
   "Ko'ruv traktining shikastlanishidan",
   "Ensa bo'lagi infarktidan"
  ],
  "izoh": "Dimlangan disk — kalla ichi gipertenziyasining muhim belgisi (o'smalar, gematoma, gidrosefaliya va h.k.)."
 },
 {
  "mavzu": "II juft",
  "savol": "O'ng ko'ruv nervi to'liq shikastlangan. O'ng ko'zga yorug'lik tushirilsa, qorachiqlar qanday javob beradi?",
  "javoblar": [
   "Ikkala qorachiq ham toraymaydi",
   "Faqat o'ng qorachiq torayadi",
   "Faqat chap qorachiq torayadi",
   "Ikkala qorachiq ham torayadi"
  ],
  "izoh": "Refleksning afferent qismi (II nerv) uzilgan. Chap ko'zga yorug'lik tushirilsa esa ikkala qorachiq torayadi, chunki efferent qism (III nerv) butun."
 },
 {
  "mavzu": "II juft",
  "savol": "Retrobulbar nevrit (ko'ruv nervining yallig'lanishi) ko'pincha qaysi kasallikning birinchi belgisi bo'ladi?",
  "javoblar": [
   "Tarqoq skleroz",
   "Miasteniya",
   "Parkinson kasalligi",
   "Siringomieliya"
  ],
  "izoh": "Retrobulbar nevrit tarqoq skleroz bemorlarining katta qismida kasallikning ilk ko'rinishi bo'lishi mumkin: ko'rishning keskin pasayishi, markaziy skotoma, ko'z harakatida og'riq."
 },
 {
  "mavzu": "II juft",
  "savol": "Ko'ruv maydonining cheklangan qismida ko'rishning yo'qolishi qanday ataladi?",
  "javoblar": [
   "Skotoma",
   "Gemianopsiya",
   "Amavroz",
   "Ambliopiya"
  ],
  "izoh": "Skotoma — ko'ruv maydonidagi «dog'». Gemianopsiya — ko'ruv maydonining yarmi tushishi; amavroz — to'liq ko'rlik; ambliopiya — ko'rish o'tkirligining pasayishi."
 },
 {
  "mavzu": "III juft",
  "savol": "Ko'zni harakatlantiruvchi nerv yadrolari qayerda joylashgan?",
  "javoblar": [
   "O'rta miyada, to'rt tepalikning yuqori tepaliklari sathida",
   "Varoliy ko'prigida, yuz nervi do'ngligi sohasida",
   "O'rta miyada, pastki tepaliklar sathida",
   "Uzunchoq miyada"
  ],
  "izoh": "III nerv yadrolari o'rta miya qopqog'ida, Silviy suv yo'li ostida, yuqori tepaliklar sathida yotadi."
 },
 {
  "mavzu": "III juft",
  "savol": "Yakubovich-Edinger-Vestfal yadrosi qanday funksiyani ta'minlaydi?",
  "javoblar": [
   "Qorachiqni toraytiruvchi va kiprikli muskullarni parasimpatik innervatsiyalaydi",
   "Qorachiqni kengaytiruvchi muskulni innervatsiyalaydi",
   "Konvergensiyani ta'minlaydi",
   "Yuqori qovoqni ko'taruvchi muskulni innervatsiyalaydi"
  ],
  "izoh": "Mayda hujayrali parasimpatik yadro: tolalar kiprikli tugun orqali m. sphincter pupillae (mioz) va m. ciliaris (akkomodatsiya) ga boradi."
 },
 {
  "mavzu": "III juft",
  "savol": "Perlia yadrosi (markaziy toq yadro) qanday funksiyani ta'minlaydi?",
  "javoblar": [
   "Ko'zlar konvergensiyasini",
   "Qorachiqning yorug'likka reaksiyasini",
   "Nigohni vertikal yo'nalishda harakatlantirishni",
   "Qovoqni ko'tarishni"
  ],
  "izoh": "Perlia yadrosi ikkala medial to'g'ri muskulning bir vaqtda qisqarishini — konvergensiyani ta'minlaydi."
 },
 {
  "mavzu": "III juft",
  "savol": "Quyidagi muskullardan qaysi biri ko'zni harakatlantiruvchi nerv (III) bilan innervatsiyalanmaydi?",
  "javoblar": [
   "Yuqori qiyshiq muskul",
   "Yuqori to'g'ri muskul",
   "Pastki qiyshiq muskul",
   "Yuqori qovoqni ko'taruvchi muskul"
  ],
  "izoh": "Yuqori qiyshiq muskulni IV nerv, lateral to'g'ri muskulni VI nerv innervatsiyalaydi. Qolgan tashqi muskullar va qovoq ko'taruvchi muskul — III nerv."
 },
 {
  "mavzu": "III juft",
  "savol": "Ko'zni harakatlantiruvchi nerv kalla bo'shlig'idan ko'z kosasiga qaysi teshik orqali chiqadi?",
  "javoblar": [
   "Yuqori ko'z yorig'i (fissura orbitalis superior)",
   "Ko'ruv kanali",
   "Pastki ko'z yorig'i",
   "Yirtilgan teshik"
  ],
  "izoh": "III, IV, VI nervlar va V nervning ko'z shoxi yuqori ko'z yorig'idan o'tadi."
 },
 {
  "mavzu": "III juft",
  "savol": "III nervning to'liq shikastlanishiga qaysi belgilar majmuasi xos?",
  "javoblar": [
   "Ptoz, tashqi g'ilaylik, midriaz, akkomodatsiya falaji",
   "Ptoz, mioz, enoftalm",
   "Ichki g'ilaylik, ko'zni tashqariga burishning imkonsizligi",
   "Pastga qaraganda diplopiya, boshni yelkaga egish"
  ],
  "izoh": "III nerv falaji: ptoz, divergent g'ilaylik, qorachiq kengayishi va fotoreaksiyaning yo'qolishi, akkomodatsiya buzilishi, diplopiya."
 },
 {
  "mavzu": "III juft",
  "savol": "III nerv to'liq falajida ko'z olmasi qaysi holatda bo'ladi?",
  "javoblar": [
   "Pastga va tashqariga og'gan",
   "Ichkariga og'gan",
   "Yuqoriga va ichkariga og'gan",
   "O'rtada, harakatsiz"
  ],
  "izoh": "Lateral to'g'ri (VI) va yuqori qiyshiq (IV) muskullar tonusi ustun keladi — ko'z pastga va tashqariga tortiladi."
 },
 {
  "mavzu": "III juft",
  "savol": "Shu tomonda III nerv falaji va qarama-qarshi tomonda markaziy gemiplegiya qaysi sindrom?",
  "javoblar": [
   "Veber sindromi",
   "Benedikt sindromi",
   "Miyyar-Gubler sindromi",
   "Valenberg-Zaxarchenko sindromi"
  ],
  "izoh": "Veber sindromi — o'rta miya oyoqchasi asosining shikastlanishi (III nerv ildizi va piramida yo'li)."
 },
 {
  "mavzu": "III juft",
  "savol": "Shu tomonda III nerv falaji va qarama-qarshi tomonda giperkinez hamda intension tremor qaysi sindromga xos?",
  "javoblar": [
   "Benedikt sindromi",
   "Veber sindromi",
   "Foster-Kennedi sindromi",
   "Parino sindromi"
  ],
  "izoh": "Benedikt sindromi — o'rta miya qopqog'ida III nerv va qizil yadroning birga shikastlanishi."
 },
 {
  "mavzu": "III juft",
  "savol": "Qorachiqning yorug'likka reaksiyasi refleks yoyining efferent qismi qaysi tolalardan iborat?",
  "javoblar": [
   "III nervning parasimpatik tolalari (kiprikli tugun orqali)",
   "Ko'ruv nervi tolalari",
   "Simpatik tolalar (yuqori bo'yin tuguni orqali)",
   "Uch shoxli nervning ko'z shoxi"
  ],
  "izoh": "Afferent — II nerv, markaz — pretektal soha va Yakubovich-Edinger-Vestfal yadrosi, efferent — III nerv parasimpatik tolalari → m. sphincter pupillae."
 },
 {
  "mavzu": "III juft",
  "savol": "Qorachiqning yorug'likka reaksiyasi yo'qolib, konvergensiya va akkomodatsiyaga reaksiyasi saqlanishi nima deyiladi?",
  "javoblar": [
   "Argayll-Robertson sindromi",
   "Eydi sindromi",
   "Bernar-Horner sindromi",
   "Parino sindromi"
  ],
  "izoh": "Argayll-Robertson sindromi klassik tarzda neyrosifilisda (orqa miya quruqshog'i) uchraydi, qorachiqlar tor va notekis bo'ladi."
 },
 {
  "mavzu": "III juft",
  "savol": "Orqa biriktiruvchi arteriya anevrizmasi III nervni ezganda eng erta paydo bo'ladigan belgi qaysi?",
  "javoblar": [
   "Shu tomonda qorachiq kengayishi (midriaz)",
   "Ptoz",
   "Ichki g'ilaylik",
   "Qarama-qarshi gemiplegiya"
  ],
  "izoh": "Parasimpatik (qorachiq) tolalari nerv stvolining yuzaki qismida joylashgan, shu sababli tashqi ezilishda birinchi bo'lib midriaz paydo bo'ladi."
 },
 {
  "mavzu": "III juft",
  "savol": "Qandli diabetda III nervning ishemik neyropatiyasi uchun nima xos?",
  "javoblar": [
   "Qorachiq funksiyasi odatda saqlanadi",
   "Birinchi navbatda midriaz paydo bo'ladi",
   "Faqat qovoq ko'taruvchi muskul shikastlanadi",
   "Albatta qarama-qarshi gemiplegiya qo'shiladi"
  ],
  "izoh": "Ishemiya asosan nerv stvolining markaziy qismini zararlaydi, yuzaki joylashgan qorachiq tolalari saqlanib qoladi («qorachiqni ayovchi» falaj)."
 },
 {
  "mavzu": "IV juft",
  "savol": "G'altak nerv (IV) qaysi muskulni innervatsiyalaydi?",
  "javoblar": [
   "Yuqori qiyshiq muskul",
   "Pastki qiyshiq muskul",
   "Lateral to'g'ri muskul",
   "Medial to'g'ri muskul"
  ],
  "izoh": "N. trochlearis faqat bitta muskulni — m. obliquus superior'ni innervatsiyalaydi."
 },
 {
  "mavzu": "IV juft",
  "savol": "G'altak nervning anatomik o'ziga xosligi nimada?",
  "javoblar": [
   "Miya stvolining orqa (dorsal) yuzasidan chiqadigan va to'liq kesishadigan yagona nerv",
   "Kalla bo'shlig'idagi eng qisqa nerv",
   "Parasimpatik tolalar tutadigan yagona ko'z nervi",
   "Kavernoz sinus ichidan o'tadigan yagona nerv"
  ],
  "izoh": "IV nerv tolalari yuqori miya parusida to'liq kesishib, stvolning dorsal yuzasidan chiqadi; u eng ingichka va kalla ichidagi yo'li eng uzun nervlardan biri."
 },
 {
  "mavzu": "IV juft",
  "savol": "G'altak nerv yadrosi qayerda joylashgan?",
  "javoblar": [
   "O'rta miyada, pastki tepaliklar sathida",
   "O'rta miyada, yuqori tepaliklar sathida",
   "Varoliy ko'prigida",
   "Uzunchoq miyada"
  ],
  "izoh": "IV nerv yadrosi III nerv yadrolaridan pastroqda, pastki tepaliklar sathida, Silviy suv yo'li ostida joylashgan."
 },
 {
  "mavzu": "IV juft",
  "savol": "Yuqori qiyshiq muskulning asosiy funksiyasi qaysi?",
  "javoblar": [
   "Ko'z olmasini pastga va tashqariga buradi",
   "Ko'z olmasini yuqoriga va tashqariga buradi",
   "Ko'z olmasini ichkariga buradi",
   "Yuqori qovoqni ko'taradi"
  ],
  "izoh": "M. obliquus superior ko'zni pastga-tashqariga buradi va ichkariga aylantiradi (intorsiya), ayniqsa ko'z ichkariga burilganda pastga qaratadi."
 },
 {
  "mavzu": "IV juft",
  "savol": "G'altak nerv shikastlanganda diplopiya qachon kuchayadi?",
  "javoblar": [
   "Pastga qaraganda (zinadan tushishda, kitob o'qishda)",
   "Yuqoriga qaraganda",
   "Shikastlangan tomonga gorizontal qaraganda",
   "Uzoqqa qaraganda"
  ],
  "izoh": "Yuqori qiyshiq muskul falajida vertikal diplopiya pastga qaraganda kuchayadi — bemorlar zinadan tushishda qiynalishadi."
 },
 {
  "mavzu": "IV juft",
  "savol": "G'altak nerv falajida bemor diplopiyani kamaytirish uchun boshini qanday tutadi?",
  "javoblar": [
   "Sog' tomonga (qarama-qarshi yelkaga) egadi",
   "Shikastlangan tomonga egadi",
   "Orqaga tashlaydi",
   "Hech qanday majburiy holat bo'lmaydi"
  ],
  "izoh": "Boshni sog' tomonga egish ekstorsiyani kompensatsiya qiladi. Boshni shikastlangan tomonga egganda diplopiya kuchayadi (Bilshovskiy sinamasi)."
 },
 {
  "mavzu": "VI juft",
  "savol": "Uzoqlashtiruvchi nerv (VI) yadrosi qayerda joylashgan?",
  "javoblar": [
   "Varoliy ko'prigida, yuz nervi do'ngligi (colliculus facialis) ostida",
   "O'rta miyada, yuqori tepaliklar sathida",
   "O'rta miyada, pastki tepaliklar sathida",
   "Uzunchoq miyada, olivalar sathida"
  ],
  "izoh": "VI nerv yadrosi ko'prik qopqog'ida yotadi; yuz nervi tolalari uni aylanib o'tib, colliculus facialis'ni hosil qiladi."
 },
 {
  "mavzu": "VI juft",
  "savol": "Uzoqlashtiruvchi nerv qaysi muskulni innervatsiyalaydi?",
  "javoblar": [
   "Lateral to'g'ri muskul",
   "Medial to'g'ri muskul",
   "Yuqori qiyshiq muskul",
   "Pastki to'g'ri muskul"
  ],
  "izoh": "N. abducens faqat m. rectus lateralis'ni innervatsiyalaydi — ko'zni tashqariga buradi."
 },
 {
  "mavzu": "VI juft",
  "savol": "VI nerv shikastlanishining asosiy belgilari qaysilar?",
  "javoblar": [
   "Ichki (konvergent) g'ilaylik, ko'zni tashqariga burishning cheklanishi, gorizontal diplopiya",
   "Tashqi g'ilaylik, ptoz, midriaz",
   "Pastga qaraganda vertikal diplopiya",
   "Ptoz, mioz, enoftalm"
  ],
  "izoh": "Medial to'g'ri muskul tonusi ustun keladi — ko'z ichkariga og'adi; diplopiya shikastlangan tomonga qaraganda kuchayadi."
 },
 {
  "mavzu": "VI juft",
  "savol": "Kalla ichi bosimi oshganda qaysi nerv ko'pincha shikastlanadi (lokal ahamiyatga ega bo'lmagan belgi sifatida)?",
  "javoblar": [
   "Uzoqlashtiruvchi nerv (VI)",
   "G'altak nerv (IV)",
   "Hid bilish nervi (I)",
   "Ko'zni harakatlantiruvchi nerv (III)"
  ],
  "izoh": "VI nervning kalla ichidagi yo'li uzun va chakka suyagi piramidasining uchi ustidan egilib o'tadi, shuning uchun bosim oshganda oson eziladi."
 },
 {
  "mavzu": "VI juft",
  "savol": "Shu tomonda VI va VII nervlarning periferik falaji hamda qarama-qarshi tomonda gemiplegiya miya stvolining qaysi bo'limi shikastlanganini ko'rsatadi?",
  "javoblar": [
   "Varoliy ko'prigi",
   "O'rta miya",
   "Uzunchoq miya",
   "Oraliq miya"
  ],
  "izoh": "Bu ko'prik sathidagi almashinuvchi sindromlar (Miyyar-Gubler, Fovil) uchun xos: VI va VII nerv yadrolari ko'prikda joylashgan."
 },
 {
  "mavzu": "III/IV/VI",
  "savol": "Kavernoz sinusning devoridan emas, bevosita bo'shlig'idan (ichki uyqu arteriyasi yonidan) o'tadigan nerv qaysi?",
  "javoblar": [
   "Uzoqlashtiruvchi nerv (VI)",
   "Ko'zni harakatlantiruvchi nerv (III)",
   "G'altak nerv (IV)",
   "Uch shoxli nervning ko'z shoxi"
  ],
  "izoh": "III, IV va V1 kavernoz sinusning lateral devorida yotadi, VI nerv esa sinus ichidan o'tadi — shuning uchun sinus trombozi va anevrizmalarida ko'pincha birinchi shikastlanadi."
 },
 {
  "mavzu": "III/IV/VI",
  "savol": "Yuqori ko'z yorig'i sindromiga qaysi belgilar majmuasi xos?",
  "javoblar": [
   "To'liq oftalmoplegiya, ptoz, midriaz va peshona sohasida sezuvchanlik buzilishi",
   "Bitemporal gemianopsiya va anosmiya",
   "Faqat ichki g'ilaylik va diplopiya",
   "Ptoz, mioz va enoftalm"
  ],
  "izoh": "Yuqori ko'z yorig'idan III, IV, VI nervlar va V nervning ko'z shoxi o'tadi — hammasi birga shikastlanadi."
 },
 {
  "mavzu": "III/IV/VI",
  "savol": "Medial bo'ylama tutam (fasciculus longitudinalis medialis) shikastlanganda qanday holat yuzaga keladi?",
  "javoblar": [
   "Internuklear oftalmoplegiya",
   "Argayll-Robertson sindromi",
   "Foster-Kennedi sindromi",
   "Bitemporal gemianopsiya"
  ],
  "izoh": "Medial bo'ylama tutam VI nerv yadrosini qarama-qarshi III nerv yadrosi bilan bog'laydi. Yon tomonga qarashda ko'z ichkariga burilmaydi, qarama-qarshi ko'zda nistagm; konvergensiya saqlanadi."
 }
]''')


def _build_questions():
    """Har bir savol uchun javob variantlarini DETERMINISTIK (doim bir xil)
    tartibda aralashtiradi — shunda /questions va /calculate bir xil kalit
    tartibiga tayanadi, lekin foydalanuvchi uchun "to'g'ri javob doim birinchi"
    degan naqsh ko'rinmaydi."""
    letters = ["A", "B", "C", "D"]
    questions = []
    for i, item in enumerate(_RAW):
        rnd = random.Random(20260101 + i)
        correct_text = item["javoblar"][0]
        shuffled = list(item["javoblar"])
        rnd.shuffle(shuffled)
        options = [{"key": letters[k], "text": t} for k, t in enumerate(shuffled)]
        correct_key = letters[shuffled.index(correct_text)]
        questions.append({
            "id": i,
            "categoryLabel": item["mavzu"],
            "prompt": item["savol"],
            "options": options,
            "correctKey": correct_key,
            "izoh": item["izoh"],
        })
    return questions


_QUESTIONS = _build_questions()


def get_questions():
    return [
        {
            "id": q["id"],
            "categoryLabel": q["categoryLabel"],
            "prompt": q["prompt"],
            "options": q["options"],
        }
        for q in _QUESTIONS
    ]


def calculate(answers):
    if not isinstance(answers, list) or len(answers) != len(_QUESTIONS):
        raise ValueError("Javoblar soni savollar soniga mos emas")

    correct_count = 0
    breakdown = {}
    details = []

    for q, ans in zip(_QUESTIONS, answers):
        is_correct = ans == q["correctKey"]
        if is_correct:
            correct_count += 1

        topic = q["categoryLabel"]
        b = breakdown.setdefault(topic, {"mavzu": topic, "correct": 0, "total": 0})
        b["total"] += 1
        if is_correct:
            b["correct"] += 1

        details.append({
            "prompt": q["prompt"],
            "options": q["options"],
            "yourKey": ans,
            "correctKey": q["correctKey"],
            "isCorrect": is_correct,
            "izoh": q["izoh"],
        })

    total = len(_QUESTIONS)
    percent = round(correct_count / total * 100)

    if percent >= 90:
        level = "A'lo darajada bilasiz"
    elif percent >= 75:
        level = "Yaxshi bilasiz"
    elif percent >= 50:
        level = "O'rtacha — takrorlash foydali"
    else:
        level = "Mavzuni qaytadan o'rganish tavsiya etiladi"

    return {
        "correct": correct_count,
        "total": total,
        "percent": percent,
        "level": level,
        "breakdown": list(breakdown.values()),
        "details": details,
    }
