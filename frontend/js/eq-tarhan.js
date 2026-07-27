RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/eq-tarhan/questions",
  submitUrl: "/api/eq-tarhan",
  parseAnswer: (v) => Number(v),
  renderResult(data) {
    const pct = Math.round(((data.total - data.min) / (data.max - data.min)) * 100);
    const adviceHtml = data.advice.map((a) => `<li>${a}</li>`).join("");

    return `
      <div class="panel">
        <div class="result-title">❤️ Sizning natijangiz</div>
        <div class="result-sub">Muallif: ${data.author}</div>
        <div class="stat-row"><strong>Daraja</strong><strong>${data.level} (${data.total}/${data.max})</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${pct}%"></div></div>
        <p>${data.summary}</p>

        <div class="meaning-row"><span class="icon">💡</span><span><strong>Maslahatlar:</strong>
          <ul class="plain">${adviceHtml}</ul>
        </span></div>

        <p class="text-muted" style="font-size:0.8rem;">${data.scale_note}</p>

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
