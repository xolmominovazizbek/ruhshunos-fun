RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/cranial-nerves/questions",
  submitUrl: "/api/cranial-nerves",
  renderResult(data) {
    const breakdownHtml = data.breakdown.map((b) => {
      const pct = Math.round((b.correct / b.total) * 100);
      return `
        <div class="breakdown-item">
          <div class="label-row">
            <span>${b.mavzu}</span>
            <span>${b.correct} / ${b.total} (${pct}%)</span>
          </div>
          <div class="progress"><div class="progress-fill" style="width:${pct}%"></div></div>
        </div>
      `;
    }).join("");

    const reviewHtml = data.details.map((d, i) => {
      const chosen = d.options.find((o) => o.key === d.yourKey);
      const correct = d.options.find((o) => o.key === d.correctKey);
      return `
        <div class="review-item ${d.isCorrect ? "review-correct" : "review-wrong"}">
          <p class="review-q"><strong>${i + 1}.</strong> ${d.prompt}</p>
          <p class="review-a">Sizning javobingiz: ${chosen ? chosen.text : "—"} ${d.isCorrect ? "✅" : "❌"}</p>
          ${!d.isCorrect ? `<p class="review-a">To'g'ri javob: ${correct ? correct.text : "—"}</p>` : ""}
          <p class="review-note">💡 ${d.izoh}</p>
        </div>
      `;
    }).join("");

    return `
      <div class="panel">
        <div class="result-title">🧠 Natijangiz: ${data.correct} / ${data.total} (${data.percent}%)</div>
        <div class="result-sub">${data.level}</div>

        <h3 style="margin-top:22px">Mavzular kesimida</h3>
        ${breakdownHtml}

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>

      <div class="panel" style="margin-top:16px;">
        <h3>Barcha savollar — to'liq ko'rib chiqish</h3>
        ${reviewHtml}
      </div>
    `;
  },
});
