RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/stai/questions",
  submitUrl: "/api/stai",
  parseAnswer: (v) => Number(v),
  renderResult(data) {
    const bandColor = (band) => (band === "Yuqori" ? "var(--danger)" : band === "O'rtacha" ? "var(--gold-dark)" : "var(--teal)");

    return `
      <div class="panel">
        <div class="result-title">📋 Spilberger-Xanin natijangiz</div>

        <h3 style="margin-top:10px">Vaziyatli xavotirlilik (ST) — hozirgi holat</h3>
        <div class="stat-row"><strong>${data.stBand}</strong><strong>${data.st} ball</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${Math.min(100, Math.round((data.st / 80) * 100))}%; background:${bandColor(data.stBand)};"></div></div>

        <h3 style="margin-top:22px">Shaxsiy xavotirlilik (LT) — odatdagi holat</h3>
        <div class="stat-row"><strong>${data.ltBand}</strong><strong>${data.lt} ball</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${Math.min(100, Math.round((data.lt / 80) * 100))}%; background:${bandColor(data.ltBand)};"></div></div>

        <p class="text-muted" style="font-size:0.85rem; margin-top:14px;">Shkala: 20-30 ball — past, 31-44 — o'rtacha, 45 va undan yuqori — yuqori xavotirlilik.</p>
        <p class="text-muted" style="font-size:0.8rem;">Manba: ${data.source}</p>

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
