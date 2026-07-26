RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/temperament/questions",
  submitUrl: "/api/temperament",
  renderResult(data) {
    const d = data.dominant;
    const breakdownHtml = data.scores.map((r) => `
      <div class="breakdown-item">
        <div class="label-row"><span>${r.key}</span><span>${r.score} (${r.pct}%)</span></div>
        <div class="progress"><div class="progress-fill" style="width:${r.pct}%"></div></div>
      </div>
    `).join("");

    return `
      <div class="panel">
        <div class="result-title">🧠 ${d.label}</div>
        <div class="result-sub">${d.trait}</div>
        <p>${d.desc}</p>

        <div class="meaning-row"><span class="icon">💼</span><span><strong>Mos kasblar:</strong> ${d.career}</span></div>
        <div class="meaning-row"><span class="icon">💞</span><span><strong>Munosabatlar:</strong> ${d.relationship}</span></div>
        <div class="meaning-row"><span class="icon">⚠️</span><span><strong>E'tibor bering:</strong> ${d.caution}</span></div>
        <div class="meaning-row"><span class="icon">💡</span><span><strong>Maslahat:</strong> ${d.advice}</span></div>

        <h3 style="margin-top:22px">4 temperament bo'yicha taqsimot</h3>
        ${breakdownHtml}

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
