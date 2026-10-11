RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/gad7/questions",
  submitUrl: "/api/gad7",
  parseAnswer: (v) => Number(v),
  renderResult(data) {
    const pct = Math.round((data.total / data.max) * 100);
    const cutoffHtml = data.clinicalCutoff
      ? `<div class="meaning-row"><span class="icon">⚠️</span><span><strong>Klinik chegaradan yuqori:</strong> bu ko'rsatkich bilan psixolog yoki psixiatr bilan suhbatlashish tavsiya etiladi — bu tashxis emas, faqat signal.</span></div>`
      : "";

    return `
      <div class="panel">
        <div class="result-title">😰 GAD-7 natijangiz</div>
        <div class="stat-row"><strong>Daraja</strong><strong>${data.level} (${data.total}/${data.max})</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${pct}%"></div></div>
        <p>${data.summary}</p>
        ${cutoffHtml}
        <p class="text-muted" style="font-size:0.8rem; margin-top:10px;">Manba: ${data.source}</p>

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
