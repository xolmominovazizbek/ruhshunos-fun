RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/hads/questions",
  submitUrl: "/api/hads",
  parseAnswer: (v) => Number(v),
  renderResult(data) {
    const badgeColor = (band) =>
      band === "Klinik" ? "var(--danger)" : band === "Subklinik" ? "var(--gold-dark)" : "var(--teal)";

    return `
      <div class="panel">
        <div class="result-title">🩺 HADS natijangiz</div>
        <div class="result-sub">Baholash sanasi: ${new Date().toLocaleDateString("uz-UZ", { year: "numeric", month: "long", day: "numeric" })}</div>

        <h3 style="margin-top:18px">Xavotir shkalasi (HADS-A)</h3>
        <div class="stat-row"><strong style="color:${badgeColor(data.bandA)};">${data.bandA}</strong><strong>${data.scoreA} / 21</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${Math.round((data.scoreA / 21) * 100)}%; background:${badgeColor(data.bandA)};"></div></div>
        <p>${data.descA}</p>

        <h3 style="margin-top:22px">Depressiya shkalasi (HADS-D)</h3>
        <div class="stat-row"><strong style="color:${badgeColor(data.bandD)};">${data.bandD}</strong><strong>${data.scoreD} / 21</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${Math.round((data.scoreD / 21) * 100)}%; background:${badgeColor(data.bandD)};"></div></div>
        <p>${data.descD}</p>

        <div class="meaning-row" style="margin-top:14px;"><span class="icon">📏</span><span><strong>Rasmiy kesim balllari:</strong> 0-7 me'yor · 8-10 subklinik · 11-21 klinik darajadagi aksentuatsiya.</span></div>
        <p class="text-muted" style="font-size:0.8rem; margin-top:10px;">Manba: ${data.source}</p>

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
