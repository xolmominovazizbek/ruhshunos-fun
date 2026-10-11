RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/phq9/questions",
  submitUrl: "/api/phq9",
  parseAnswer: (v) => Number(v),
  renderResult(data) {
    const pct = Math.round((data.total / data.max) * 100);
    const cutoffHtml = data.clinicalCutoff
      ? `<div class="meaning-row"><span class="icon">⚠️</span><span><strong>Klinik chegaradan yuqori:</strong> bu ko'rsatkich bilan psixolog yoki psixiatr bilan suhbatlashish tavsiya etiladi — bu tashxis emas, faqat signal.</span></div>`
      : "";

    // Xavfsizlik bayrog'i: 9-savolga (o'z joniga zarar fikrlari) har qanday
    // ijobiy javob berilgan bo'lsa, yordam bloki albatta ko'rsatiladi —
    // umumiy balldan qat'i nazar.
    const safetyEl = document.getElementById("safety-help");
    if (safetyEl) {
      if (data.safetyFlag) {
        safetyEl.classList.remove("hidden");
      } else {
        safetyEl.classList.add("hidden");
      }
    }

    const safetyNoticeHtml = data.safetyFlag
      ? `<div class="meaning-row" style="background:var(--danger-soft); border-radius:var(--radius-sm); padding:12px;"><span class="icon">🆘</span><span><strong>Muhim:</strong> 9-savolingizga bergan javobingiz sababli, pastdagi yordam raqamlariga alohida e'tibor qarating.</span></div>`
      : "";

    return `
      <div class="panel">
        <div class="result-title">🌧️ PHQ-9 natijangiz</div>
        <div class="stat-row"><strong>Daraja</strong><strong>${data.level} (${data.total}/${data.max})</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${pct}%"></div></div>
        <p>${data.summary}</p>
        ${safetyNoticeHtml}
        ${cutoffHtml}
        <p class="text-muted" style="font-size:0.8rem; margin-top:10px;">Manba: ${data.source}</p>

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>
    `;
  },
});
