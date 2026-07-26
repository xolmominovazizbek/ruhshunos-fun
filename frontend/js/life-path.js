const form = document.getElementById("life-path-form");
const resultEl = document.getElementById("result");
const errorEl = document.getElementById("error");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorEl.classList.add("hidden");
  resultEl.classList.add("hidden");

  const formData = new FormData(form);
  const payload = { birth_date: formData.get("birth_date") };

  try {
    const res = await fetch("/api/life-path", {
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
  const m = data.meaning;
  const masterBadge = data.is_master
    ? `<div class="badge" style="margin-bottom:12px">✨ Master son!</div>`
    : "";

  const html = `
    <div class="panel">
      <div class="result-title">🔢 SIZNING HAYOT SONINGIZ</div>
      <div class="calc-box">${data.calculation}</div>

      <div style="display:flex; align-items:center; gap:16px; margin-bottom:16px">
        <div class="number-badge">${data.number}</div>
        <div>
          ${masterBadge}
          <div style="font-size:1.2rem; font-weight:700">${m.title}</div>
        </div>
      </div>

      <p>${m.summary}</p>

      <div class="meaning-row"><span class="icon">💼</span><span><strong>Kasb:</strong> ${m.career}</span></div>
      <div class="meaning-row"><span class="icon">💞</span><span><strong>Munosabatlar:</strong> ${m.relationships}</span></div>
      <div class="meaning-row"><span class="icon">🧠</span><span><strong>Kuchli tomonlar:</strong> ${m.strengths}</span></div>
      <div class="meaning-row"><span class="icon">⚠️</span><span><strong>E'tibor bering:</strong> ${m.caution}</span></div>
      <div class="meaning-row"><span class="icon">💡</span><span><strong>Maslahat:</strong> ${m.advice}</span></div>
    </div>
  `;

  resultEl.innerHTML = html;
  resultEl.classList.remove("hidden");
  resultEl.scrollIntoView({ behavior: "smooth", block: "start" });
}
