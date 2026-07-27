/**
 * Barcha savol-javob (A/B tanlov yoki Likert shkala) testlari uchun umumiy
 * bosqichma-bosqich (stepper) mexanizm. Har bir test sahifasi (love-language.js,
 * temperament.js, eq.js, stress.js) shu funksiyani chaqirib, faqat natijani
 * chizish (renderResult) qismini o'zi ta'minlaydi.
 */
window.RuhshunosQuiz = (function () {
  function createStepper({ mount, questions, onFinish }) {
    const answers = new Array(questions.length).fill(null);
    let idx = 0;

    function render() {
      const q = questions[idx];
      mount.innerHTML = `
        <div class="quiz-progress">
          <div class="progress"><div class="progress-fill" style="width:${((idx + 1) / questions.length) * 100}%"></div></div>
          <span class="quiz-step-label">${idx + 1} / ${questions.length}</span>
        </div>
        <div class="quiz-card">
          ${q.categoryLabel ? `<p class="text-muted" style="font-size:0.8rem; font-weight:700; text-transform:uppercase; letter-spacing:.04em; margin:0 0 8px;">${q.categoryLabel}</p>` : ""}
          <p class="quiz-prompt">${q.prompt}</p>
          <div class="quiz-options" role="group"></div>
          <div class="quiz-nav">
            <button type="button" class="quiz-back" ${idx === 0 ? "disabled" : ""}>← Oldingi savol</button>
          </div>
        </div>
      `;
      const optionsEl = mount.querySelector(".quiz-options");
      q.options.forEach((opt) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "quiz-option";
        btn.setAttribute("aria-pressed", String(answers[idx] === opt.key));
        btn.innerHTML = `<span class="dot"></span><span>${opt.text}</span>`;
        btn.addEventListener("click", () => {
          answers[idx] = opt.key;
          if (idx < questions.length - 1) {
            idx += 1;
            render();
          } else {
            onFinish(answers);
          }
        });
        optionsEl.appendChild(btn);
      });
      mount.querySelector(".quiz-back").addEventListener("click", () => {
        if (idx > 0) { idx -= 1; render(); }
      });
      mount.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    render();
  }

  async function start({ introId, quizMountId, resultMountId, errorId, startButtonId, questionsUrl, submitUrl, parseAnswer, renderResult }) {
    const introEl = document.getElementById(introId);
    const quizEl = document.getElementById(quizMountId);
    const resultEl = document.getElementById(resultMountId);
    const errorEl = document.getElementById(errorId);
    const startBtn = document.getElementById(startButtonId);

    function showError(message) {
      errorEl.textContent = message;
      errorEl.classList.remove("hidden");
    }

    startBtn.addEventListener("click", async () => {
      errorEl.classList.add("hidden");
      startBtn.disabled = true;
      startBtn.textContent = "Yuklanmoqda...";
      try {
        const res = await fetch(questionsUrl);
        if (!res.ok) throw new Error("Savollarni yuklab bo'lmadi");
        const questions = await res.json();

        introEl.classList.add("hidden");
        quizEl.classList.remove("hidden");

        createStepper({
          mount: quizEl,
          questions,
          onFinish: async (rawAnswers) => {
            const answers = parseAnswer ? rawAnswers.map(parseAnswer) : rawAnswers;
            quizEl.innerHTML = '<p class="text-muted">Natija hisoblanmoqda...</p>';
            try {
              const submitRes = await fetch(submitUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ answers }),
              });
              if (!submitRes.ok) {
                const err = await submitRes.json().catch(() => ({}));
                throw new Error(err.detail || "Xatolik yuz berdi");
              }
              const data = await submitRes.json();
              quizEl.innerHTML = "";
              quizEl.classList.add("hidden");
              resultEl.innerHTML = renderResult(data);
              resultEl.classList.remove("hidden");
              const retakeBtn = resultEl.querySelector(".retake");
              if (retakeBtn) {
                retakeBtn.addEventListener("click", () => {
                  resultEl.classList.add("hidden");
                  resultEl.innerHTML = "";
                  introEl.classList.remove("hidden");
                  startBtn.disabled = false;
                  startBtn.textContent = "Testni boshlash";
                });
              }
              resultEl.scrollIntoView({ behavior: "smooth", block: "start" });
            } catch (err) {
              quizEl.classList.add("hidden");
              introEl.classList.remove("hidden");
              startBtn.disabled = false;
              startBtn.textContent = "Testni boshlash";
              showError(err.message);
            }
          },
        });
      } catch (err) {
        introEl.classList.remove("hidden");
        startBtn.disabled = false;
        startBtn.textContent = "Testni boshlash";
        showError(err.message);
      }
    });
  }

  return { start };
})();
