/* ============================================================
   Ruhshunos — Ogohlantirish matnlari (yagona manba)
   Fayl: js/disclaimer.js

   Ishlatilishi — sahifada shunchaki bitta div qoldiring:
     <div data-rs-note="fun"></div>   → ko'ngilochar testlar
     <div data-rs-note="sci"></div>   → ilmiy asosga tayangan testlar
     <div data-rs-help></div>         → yordam raqamlari bloki

   Matnni yoki raqamni o'zgartirish kerak bo'lsa — faqat shu fayl
   tahrirlanadi, 15 ta HTML sahifa emas.
   ============================================================ */

(function () {
  "use strict";

  /* ---------- 1. RAQAMLAR ----------
     ⚠️ MUHIM: har bir raqamni chiqarishdan oldin O'ZINGIZ qo'ng'iroq
     qilib tekshiring va tekshirilgan sanani yozib qo'ying.
     Ishlamaydigan raqam — ogohlantirish yo'qligidan ham xavfli.  */

  var LINES = [
    {
      name: "Tez yordam",
      meta: "Hayotga xavf tug'ilganda — 24/7",
      tel: "103",
      show: "103"
    },
    {
      name: "Respublika ruhiy salomatlik markazi",
      meta: "Toshkent — ishonch telefoni",
      tel: "+998712592137",
      show: "71 259-21-37"
    },
    {
      // TODO: Surxondaryo mintaqaviy markaz raqamini qo'shing —
      // o'zingiz ishlaydigan joy, eng ishonchli manba.
      name: "Surxondaryo mintaqaviy markaz",
      meta: "Qabul bo'limi — ish kunlari",
      tel: "+998__________",
      show: "raqam qo'shilishi kerak"
    }
  ];

  /* ---------- 2. MATNLAR ---------- */

  var NOTES = {
    fun: {
      label: "Ko'ngilochar test",
      body:
        "<p>Bu test faqat ko'ngilochar maqsadda tuzilgan. Uning ortida ilmiy " +
        "asos yo'q va natija sizning shaxsiyatingiz, qobiliyatingiz yoki " +
        "kelajagingiz haqida hech narsa aytmaydi.</p>" +
        "<p>Muhim qarorlarni — sog'liq, o'qish, ish yoki munosabatlar " +
        "haqidagi qarorlarni — bunday natijalarga tayanib qabul qilmang.</p>"
    },
    sci: {
      label: "Ilmiy konstruktga asoslangan",
      body:
        "<p>Bu test psixologiyada tan olingan tushunchalarga tayanadi, lekin " +
        "o'zbek tilidagi versiyasi hali rasmiy validatsiyadan o'tmagan. " +
        "Shuning uchun natija <strong>tashxis emas</strong> — u o'z-o'zini " +
        "kuzatish uchun yo'l ko'rsatuvchi vosita.</p>" +
        "<p>Natija sizni tashvishga solsa yoki kundalik hayotingizga " +
        "ta'sir qilayotgan holatni tasdiqlasa, psixolog yoki psixiatrga " +
        "murojaat qiling. Test shifokor o'rnini bosmaydi.</p>"
    }
  };

  var HELP = {
    title: "Yordam kerakmi?",
    lead:
      "Agar o'zingizni juda og'ir his qilsangiz, o'zingizga zarar yetkazish " +
      "haqida o'ylayotgan bo'lsangiz yoki yaqiningiz uchun xavotirdasiz — " +
      "kutmang, hoziroq qo'ng'iroq qiling. Bu holatlarda yordam so'rash " +
      "eng to'g'ri qadam.",
    foot:
      "Ruhshunos tashxis qo'ymaydi, dori tavsiya qilmaydi va shoshilinch " +
      "yordam ko'rsatmaydi. Sayt orqali yozgan xatingizga darhol javob " +
      "berilishiga kafolat yo'q — shuning uchun og'ir holatda telefondan " +
      "foydalaning."
  };

  /* ---------- 3. RENDER ---------- */

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
  }

  function renderNote(kind) {
    var n = NOTES[kind] || NOTES.fun;
    return (
      '<span class="rs-note__label">' + esc(n.label) + "</span>" + n.body
    );
  }

  function renderHelp() {
    var rows = LINES.map(function (l) {
      return (
        '<li class="rs-help__row">' +
          '<span class="rs-help__name">' + esc(l.name) +
            '<span class="rs-help__meta">' + esc(l.meta) + "</span>" +
          "</span>" +
          '<a class="rs-help__tel" href="tel:' + esc(l.tel) + '">' +
            esc(l.show) +
          "</a>" +
        "</li>"
      );
    }).join("");

    return (
      '<h2 class="rs-help__title">' + esc(HELP.title) + "</h2>" +
      '<p class="rs-help__lead">' + esc(HELP.lead) + "</p>" +
      '<ul class="rs-help__list">' + rows + "</ul>" +
      '<p class="rs-help__foot">' + esc(HELP.foot) + "</p>"
    );
  }

  function init() {
    document.querySelectorAll("[data-rs-note]").forEach(function (el) {
      var kind = el.getAttribute("data-rs-note");
      el.className = "rs-note" + (kind === "sci" ? " rs-note--sci" : " rs-note--fun");
      el.innerHTML = renderNote(kind);
    });

    document.querySelectorAll("[data-rs-help]").forEach(function (el) {
      el.className = "rs-help";
      el.setAttribute("role", "complementary");
      el.innerHTML = renderHelp();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
