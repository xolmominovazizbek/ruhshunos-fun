const form = document.getElementById("zodiac-form");
const resultEl = document.getElementById("result");
const errorEl = document.getElementById("error");

const BREAKDOWN_LABELS = {
  element: "Element mosligi",
  modality: "Modallik mosligi",
  distance: "Burjlar orasidagi masofa",
  gender: "Jins farqi koeffitsienti",
};

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorEl.classList.add("hidden");
  resultEl.classList.add("hidden");

  const formData = new FormData(form);
  const payload = {
    birth_date: formData.get("birth_date"),
    gender: formData.get("gender") || null,
  };
  const partnerDate = formData.get("partner_birth_date");
  if (partnerDate) {
    payload.partner_birth_date = partnerDate;
    payload.partner_gender = formData.get("partner_gender") || null;
  }

  try {
    const res = await fetch("/api/zodiac", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || "Xatolik yuz berdi");
    }
    const data = await res.json();
    renderResult(data);
  } catch (err) {
    errorEl.textContent = err.message;
    errorEl.classList.remove("hidden");
  }
});

function renderResult(data) {
  const { sign, compatibility } = data;

  let html = `
    <div class="panel">
      <div class="result-title">${sign.emoji} ${sign.name}</div>
      <div class="result-sub">${sign.date_range} · ${sign.element_emoji} ${sign.element} element</div>
      <p>${sign.description}</p>
    </div>
  `;

  if (compatibility) {
    const p = compatibility.partner_sign;
    let breakdownHtml = "";
    for (const [key, value] of Object.entries(compatibility.breakdown)) {
      breakdownHtml += `
        <div class="breakdown-item">
          <div class="label-row"><span>${BREAKDOWN_LABELS[key]}</span><span>${value}%</span></div>
          <div class="progress"><div class="progress-fill" style="width:${value}%"></div></div>
        </div>
      `;
    }

    const problemsHtml = compatibility.problems.map((p) => `<li>${p}</li>`).join("");

    html += `
      <div class="panel">
        <div class="result-title">🌟 SIZNING MOSLIGINGIZ</div>
        <div class="result-sub">${sign.emoji} ${sign.name} (siz) + ${p.emoji} ${p.name} (sherigingiz)</div>

        <div class="stat-row"><strong>💞 Umumiy moslik</strong><strong>${compatibility.total}%</strong></div>
        <div class="progress"><div class="progress-fill" style="width:${compatibility.total}%"></div></div>

        <p>${compatibility.summary}</p>

        <div class="meaning-row"><span class="icon">🔥</span><span><strong>Element:</strong> ${compatibility.element_note}</span></div>
        <div class="meaning-row"><span class="icon">⚡</span><span><strong>Energiya darajasi:</strong> ${compatibility.energy}</span></div>
        <div class="meaning-row"><span class="icon">💬</span><span><strong>Muloqot:</strong> ${compatibility.communication}</span></div>

        <div class="meaning-row"><span class="icon">💔</span><span><strong>Mumkin bo'lgan muammolar:</strong>
          <ul class="plain">${problemsHtml}</ul>
        </span></div>

        <div class="meaning-row"><span class="icon">💡</span><span><strong>Maslahat:</strong> ${compatibility.advice}</span></div>

        <h3 style="margin-top:24px">Mezonlar bo'yicha taqsimot</h3>
        ${breakdownHtml}
      </div>
    `;
  }

  resultEl.innerHTML = html;
  resultEl.classList.remove("hidden");
  resultEl.scrollIntoView({ behavior: "smooth", block: "start" });
}
