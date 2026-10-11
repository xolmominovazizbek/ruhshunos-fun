RuhshunosQuiz.start({
  introId: "intro",
  quizMountId: "quiz",
  resultMountId: "result",
  errorId: "error",
  startButtonId: "start-btn",
  questionsUrl: "/api/leonhard-shmishek/questions",
  submitUrl: "/api/leonhard-shmishek",
  parseAnswer: (v) => Number(v),
  renderResult(data) {
    const bandColor = (band) =>
      band === "yaqqol aksentuatsiya" ? "var(--danger)" : band === "moyillik" ? "var(--gold-dark)" : "var(--teal)";

    const rowsHtml = data.results.map((r) => `
      <div class="breakdown-item">
        <div class="label-row">
          <span>${r.icon} ${r.name}</span>
          <span>${r.score} / ${r.max} · ${r.band}</span>
        </div>
        <div class="progress"><div class="progress-fill" style="width:${Math.round((r.score / r.max) * 100)}%; background:${bandColor(r.band)};"></div></div>
      </div>
    `).join("");

    const leadingHtml = data.leading ? `
      <div class="meaning-row"><span class="icon">${data.leading.icon}</span><span><strong>Yetakchi xususiyat:</strong> ${data.leading.name} — ${data.leading.desc}</span></div>
    ` : "";

    const pronouncedHtml = data.pronounced.length ? `
      <h3 style="margin-top:22px">Yaqqol aksentuatsiya darajasidagi xususiyatlar</h3>
      ${data.pronounced.map((r) => `<div class="meaning-row"><span class="icon">${r.icon}</span><span><strong>${r.name}</strong> (${r.score}/24) — ${r.desc}</span></div>`).join("")}
    ` : `<p class="text-muted">Hech bir xususiyat "yaqqol aksentuatsiya" darajasiga (19-24 ball) yetmadi.</p>`;

    return `
      <div class="panel">
        <div class="result-title">🎭 Xarakter aksentuatsiyasi profilingiz</div>
        <div class="result-sub">10 shkala bo'yicha natijalar (0-12 me'yor · 13-18 moyillik · 19-24 yaqqol aksentuatsiya)</div>
        ${leadingHtml}

        <h3 style="margin-top:22px">Barcha shkalalar</h3>
        ${rowsHtml}

        <button type="button" class="primary retake">Qaytadan boshlash</button>
      </div>

      <div class="panel" style="margin-top:16px;">
        ${pronouncedHtml}
      </div>
    `;
  },
});
