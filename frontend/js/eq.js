RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/eq/questions",
  submitUrl: "/api/eq",
  parseAnswer: (v) => Number(v),
  renderResult(data) {
    const pct = Math.round(((data.overall - data.min) / (data.max - data.min)) * 100);
    const breakdownHtml = data.breakdown.map((b) => `
      <div class="breakdown-item">
        <div class="label-row"><span>${b.label}</span><span>${b.score}/${b.max} (${b.pct}%)</span></div>
        <div class="progress"><div class="progress-fill" style="width:${b.pct}%"></div></div>
      </div>
    `).join("");
    const adviceHtml = data.advice.map((a) => `<li>${a}</li>`).join("");

    return `
      <div class="panel">
        <div class="result-title">🧩 Sizning EQ profilingiz</div>
        <div class="stat-row"><strong>Daraja</strong><strong>${data.level} (${data.overall}/${data.max})</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${pct}%"></div></div>
        <p>${data.summary}</p>

        <div class="meaning-row"><span class="icon">💡</span><span><strong>Maslahatlar:</strong>
          <ul class="plain">${adviceHtml}</ul>
        </span></div>

        <h3 style="margin-top:22px">4 yo'nalish bo'yicha tahlil</h3>
        ${breakdownHtml}

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
