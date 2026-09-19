// Lógica para la práctica guiada por materias con feedback instantáneo
document.addEventListener('DOMContentLoaded', () => {
    let questions = [];
    let currentIndex = 0;
    let selectedOption = null;
    let isChecked = false;
    let correctScore = 0;
    let incorrectScore = 0;
    let currentCategory = 'all';

    // Parse URL query parameter
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('cat')) {
        currentCategory = urlParams.get('cat');
    }

    // DOM Elements
    const categoryButtons = document.querySelectorAll('.cat-filter-btn');
    const practiceLoading = document.getElementById('practice-loading');
    const practiceContainer = document.getElementById('practice-container');
    const pProgressText = document.getElementById('p-progress-text');
    const pCorrectScore = document.getElementById('p-correct-score');
    const pIncorrectScore = document.getElementById('p-incorrect-score');
    const pCategoryBadge = document.getElementById('p-category-badge');
    const pDifficultyBadge = document.getElementById('p-difficulty-badge');
    const pQuestionText = document.getElementById('p-question-text');
    const pOptionsContainer = document.getElementById('p-options-container');
    const pCheckBtn = document.getElementById('p-check-btn');
    const pNextBtn = document.getElementById('p-next-btn');
    const pJustificationBox = document.getElementById('p-justification-box');
    const pLegalBasis = document.getElementById('p-legal-basis');
    const pJustificationText = document.getElementById('p-justification-text');
    const pDistractorsText = document.getElementById('p-distractors-text');

    // Init active pill
    categoryButtons.forEach(btn => {
        if (btn.dataset.cat === currentCategory) {
            btn.classList.add('bg-blue-700', 'text-white');
            btn.classList.remove('bg-slate-100', 'text-slate-700');
        } else {
            btn.classList.remove('bg-blue-700', 'text-white');
            btn.classList.add('bg-slate-100', 'text-slate-700');
        }

        btn.addEventListener('click', () => {
            currentCategory = btn.dataset.cat;
            categoryButtons.forEach(b => {
                b.classList.remove('bg-blue-700', 'text-white');
                b.classList.add('bg-slate-100', 'text-slate-700');
            });
            btn.classList.add('bg-blue-700', 'text-white');
            btn.classList.remove('bg-slate-100', 'text-slate-700');

            loadPracticeQuestions(currentCategory);
        });
    });

    async function loadPracticeQuestions(category) {
        practiceLoading.classList.remove('hidden');
        practiceContainer.classList.add('hidden');
        currentIndex = 0;
        correctScore = 0;
        incorrectScore = 0;
        pCorrectScore.textContent = '0';
        pIncorrectScore.textContent = '0';

        try {
            const res = await fetch(`/api/practice/questions?category=${encodeURIComponent(category)}`);
            const data = await res.json();
            if (data.success && data.questions.length > 0) {
                questions = data.questions;
                practiceLoading.classList.add('hidden');
                practiceContainer.classList.remove('hidden');
                renderQuestion(0);
            } else {
                practiceLoading.innerHTML = '<div class="text-slate-500 font-medium">No se encontraron preguntas en esta materia.</div>';
            }
        } catch (err) {
            console.error('Error loading practice questions:', err);
            practiceLoading.innerHTML = '<div class="text-rose-600 font-medium">Error al cargar preguntas.</div>';
        }
    }

    function renderQuestion(index) {
        if (index < 0 || index >= questions.length) return;
        currentIndex = index;
        const q = questions[index];
        selectedOption = null;
        isChecked = false;

        pProgressText.textContent = `Caso ${index + 1} de ${questions.length}`;
        pCategoryBadge.textContent = q.category_name;
        pDifficultyBadge.innerHTML = `Dificultad: <strong class="text-slate-600">${q.difficulty || 'Media'}</strong>`;
        pQuestionText.textContent = q.question;

        // Reset justification box
        pJustificationBox.classList.add('hidden');
        pCheckBtn.classList.remove('hidden');
        pNextBtn.classList.add('hidden');

        // Render options
        pOptionsContainer.innerHTML = '';
        const opts = [
            { key: 'A', text: q.option_a },
            { key: 'B', text: q.option_b },
            { key: 'C', text: q.option_c },
            { key: 'D', text: q.option_d }
        ];

        opts.forEach(opt => {
            const card = document.createElement('div');
            card.className = 'option-card border-2 border-slate-200 hover:border-blue-400 hover:bg-blue-50/40 rounded-xl p-2.5 sm:p-3 cursor-pointer flex items-center gap-3 transition-all';
            card.dataset.option = opt.key;
            card.innerHTML = `
                <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full border-2 border-slate-300 flex items-center justify-center font-extrabold text-xs sm:text-sm text-slate-700 shrink-0 opt-indicator">
                    ${opt.key}
                </div>
                <div class="text-sm sm:text-base text-slate-800 leading-snug flex-grow font-medium">
                    ${opt.text}
                </div>
            `;

            card.addEventListener('click', () => {
                if (isChecked) return; // Cannot change after checking
                selectPracticeOption(opt.key);
            });

            pOptionsContainer.appendChild(card);
        });

        lucide.createIcons();
    }

    function selectPracticeOption(optKey) {
        if (isChecked) return;
        selectedOption = optKey;
        pOptionsContainer.querySelectorAll('.option-card').forEach(c => {
            const indicator = c.querySelector('.opt-indicator');
            if (c.dataset.option === selectedOption) {
                c.classList.add('selected', 'border-blue-600', 'bg-blue-50/80', 'ring-2', 'ring-blue-500/20');
                indicator.classList.remove('border-slate-300', 'text-slate-700');
                indicator.classList.add('border-blue-600', 'bg-blue-600', 'text-white');
            } else {
                c.classList.remove('selected', 'border-blue-600', 'bg-blue-50/80', 'ring-2', 'ring-blue-500/20');
                indicator.classList.remove('border-blue-600', 'bg-blue-600', 'text-white');
                indicator.classList.add('border-slate-300', 'text-slate-700');
            }
        });
    }

    // Keyboard Shortcuts for Practice Mode
    document.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        const key = e.key.toUpperCase();
        if (['A', '1'].includes(key)) {
            e.preventDefault();
            selectPracticeOption('A');
        } else if (['B', '2'].includes(key)) {
            e.preventDefault();
            selectPracticeOption('B');
        } else if (['C', '3'].includes(key)) {
            e.preventDefault();
            selectPracticeOption('C');
        } else if (['D', '4'].includes(key)) {
            e.preventDefault();
            selectPracticeOption('D');
        } else if (e.key === 'Enter') {
            e.preventDefault();
            if (!isChecked && selectedOption) {
                pCheckBtn.click();
            } else if (isChecked) {
                pNextBtn.click();
            }
        }
    });

    pCheckBtn.addEventListener('click', () => {
        if (!selectedOption) {
            alert('Por favor selecciona una opción antes de comprobar.');
            return;
        }

        isChecked = true;
        const q = questions[currentIndex];
        const isCorrect = (selectedOption === q.correct_option);

        if (isCorrect) {
            correctScore++;
            pCorrectScore.textContent = correctScore;
        } else {
            incorrectScore++;
            pIncorrectScore.textContent = incorrectScore;
        }

        // Highlight options
        pOptionsContainer.querySelectorAll('.option-card').forEach(c => {
            const opt = c.dataset.option;
            const indicator = c.querySelector('.opt-indicator');

            if (opt === q.correct_option) {
                c.classList.add('border-emerald-500', 'bg-emerald-50/80');
                indicator.classList.add('bg-emerald-600', 'border-emerald-600', 'text-white');
            } else if (opt === selectedOption && !isCorrect) {
                c.classList.add('border-rose-500', 'bg-rose-50/80');
                indicator.classList.add('bg-rose-600', 'border-rose-600', 'text-white');
            } else {
                c.classList.add('opacity-60');
            }
        });

        // Show legal justification
        pLegalBasis.textContent = `Base Legal: ${q.legal_basis}`;
        pJustificationText.textContent = q.justification;
        pDistractorsText.textContent = q.distractors_analysis;
        pJustificationBox.classList.remove('hidden');

        pCheckBtn.classList.add('hidden');
        if (currentIndex < questions.length - 1) {
            pNextBtn.innerHTML = `<span>Siguiente Caso</span> <i data-lucide="arrow-right" class="w-4 h-4"></i>`;
            pNextBtn.classList.remove('hidden');
        } else {
            pNextBtn.innerHTML = `<span>Finalizar Práctica</span> <i data-lucide="check" class="w-4 h-4"></i>`;
            pNextBtn.classList.remove('hidden');
        }

        lucide.createIcons();
    });

    pNextBtn.addEventListener('click', () => {
        if (currentIndex < questions.length - 1) {
            renderQuestion(currentIndex + 1);
        } else {
            alert(`¡Has completado todos los casos de esta materia!\nAciertos: ${correctScore} de ${questions.length}`);
            loadPracticeQuestions(currentCategory);
        }
    });

    // Start
    loadPracticeQuestions(currentCategory);
});
