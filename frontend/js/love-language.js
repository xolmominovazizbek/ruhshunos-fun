RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/love-language/questions",
  submitUrl: "/api/love-language",
  renderResult(data) {
    const breakdownHtml = data.scores.map((r, i) => `
      <div class="breakdown-item">
        <div class="label-row">
          <span>${r.key}${i === 0 ? " · asosiy" : i === 1 ? " · ikkinchi" : ""}</span>
          <span>${r.score} (${r.pct}%)</span>
        </div>
        <div class="progress"><div class="progress-fill" style="width:${r.pct}%"></div></div>
      </div>
    `).join("");

    return `
      <div class="panel">
        <div class="result-title">💞 Sizning sevgi profilingiz</div>
        <div class="result-sub">${data.primary} + ${data.secondary}</div>
        <p>${data.summary}</p>
        <div class="meaning-row"><span class="icon">💡</span><span><strong>Maslahat:</strong> ${data.advice}</span></div>

        <h3 style="margin-top:22px">5 tilning nisbiy ulushi</h3>
        ${breakdownHtml}

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
