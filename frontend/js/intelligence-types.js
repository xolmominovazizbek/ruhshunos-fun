const BAND_TAG = {
  "Qoniqarsiz": "🔴",
  "O'rtacha": "🟡",
  "Baland": "🟢",
  "Juda baland": "🟢",
};

RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/intelligence-types/questions",
  submitUrl: "/api/intelligence-types",
  parseAnswer: (v) => Number(v),
  renderResult(data) {
    const pct = Math.round((data.total / data.max) * 100);
    const breakdownHtml = data.breakdown.map((b) => {
      const bpct = Math.round((b.score / b.max) * 100);
      return `
        <div class="breakdown-item">
          <div class="label-row"><span>${b.icon} ${b.label}</span><span>${BAND_TAG[b.band] || ""} ${b.band} — ${b.score}/${b.max}</span></div>
          <div class="progress"><div class="progress-fill" style="width:${bpct}%"></div></div>
        </div>
      `;
    }).join("");

    const sorted = [...data.breakdown].sort((a, b) => (b.score / b.max) - (a.score / a.max));
    const top3 = sorted.slice(0, 3).map((b) => `${b.icon} ${b.label}`).join(", ");

    return `
      <div class="panel">
        <div class="result-title">🧠 Umumiy natija</div>
        <div class="stat-row"><strong>Umumiy daraja</strong><strong>${data.overallBand} (${data.total}/${data.max})</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${pct}%"></div></div>
        <p>Bolada eng yuqori ko'rsatkichlar: <strong>${top3}</strong>.</p>

        <h3 style="margin-top:22px">10 turdagi intellekt bo'yicha taqsimot</h3>
        ${breakdownHtml}

        <div class="observer-notice" style="margin-top:20px;">
          Bu natija faqat kuzatuv-yo'naltiruvchi xarakterga ega. Aniq xulosa va rivojlantirish
          bo'yicha tavsiyalar uchun klinik psixolog yoki maktab psixologi bilan maslahatlashing.
        </div>

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
