// Lógica del Simulador de Examen Oficial de Notariado CSJ
document.addEventListener('DOMContentLoaded', () => {
    let questions = [];
    let currentIndex = 0;
    let userAnswers = {}; // { qid: 'A' }
    let flaggedQuestions = new Set(); // Set of question ids
    let totalTimeSeconds = 25 * 60; // 25 minutes
    let timeRemaining = totalTimeSeconds;
    let timerInterval = null;
    let isSubmitting = false;

    // DOM Elements
    const loadingState = document.getElementById('loading-state');
    const examContainer = document.getElementById('exam-container');
    const timerDisplay = document.getElementById('timer-display');
    const timerBox = document.getElementById('timer-box');
    const currentQNum = document.getElementById('current-q-num');
    const totalQCount = document.getElementById('total-q-count');
    const categoryText = document.getElementById('category-text');
    const difficultyText = document.getElementById('difficulty-text');
    const qText = document.getElementById('q-text');
    const optionsContainer = document.getElementById('options-container');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const flagBtn = document.getElementById('flag-btn');
    const flagText = document.getElementById('flag-text');
    const finishBtn = document.getElementById('finish-btn');
    const paletteGrid = document.getElementById('palette-grid');
    const statAnswered = document.getElementById('stat-answered');
    const statUnanswered = document.getElementById('stat-unanswered');
    const statFlagged = document.getElementById('stat-flagged');
    const answeredCountBadge = document.getElementById('answered-count-badge');

    // Modal elements
    const confirmModal = document.getElementById('confirm-modal');
    const modalAnsweredCount = document.getElementById('modal-answered-count');
    const modalTotalCount = document.getElementById('modal-total-count');
    const modalUnansweredWarning = document.getElementById('modal-unanswered-warning');
    const modalUnansweredCount = document.getElementById('modal-unanswered-count');
    const modalCancelBtn = document.getElementById('modal-cancel-btn');
    const modalConfirmBtn = document.getElementById('modal-confirm-btn');

    // Fetch randomized questions from API
    async function initExam() {
        try {
            const res = await fetch('/api/exam/generate');
            const data = await res.json();
            if (!data.success || !data.questions || data.questions.length === 0) {
                alert('Error al cargar preguntas de examen.');
                return;
            }

            questions = data.questions;
            totalQCount.textContent = questions.length;
            modalTotalCount.textContent = questions.length;

            loadingState.classList.add('hidden');
            examContainer.classList.remove('hidden');

            renderPalette();
            renderQuestion(0);
            startTimer();
            lucide.createIcons();
        } catch (err) {
            console.error('Error fetching questions:', err);
            alert('Error de conexión al generar el examen.');
        }
    }

    // Render palette grid buttons (1..N)
    function renderPalette() {
        paletteGrid.innerHTML = '';
        questions.forEach((q, idx) => {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = `q-btn h-9 rounded-lg text-xs font-bold border border-slate-200 bg-white text-slate-700 hover:border-slate-400 flex items-center justify-center relative`;
            btn.textContent = idx + 1;
            btn.dataset.index = idx;
            btn.addEventListener('click', () => {
                renderQuestion(idx);
            });
            paletteGrid.appendChild(btn);
        });
        updatePalette();
    }

    // Update palette visual state
    function updatePalette() {
        const buttons = paletteGrid.querySelectorAll('.q-btn');
        let answeredCount = 0;
        let flaggedCount = 0;

        buttons.forEach((btn, idx) => {
            const q = questions[idx];
            const isAnswered = userAnswers.hasOwnProperty(q.id);
            const isFlagged = flaggedQuestions.has(q.id);
            const isCurrent = idx === currentIndex;

            // Reset base classes
            btn.className = `q-btn h-9 rounded-lg text-xs font-bold flex items-center justify-center relative transition-all`;

            if (isCurrent) {
                btn.classList.add('ring-2', 'ring-navy-900', 'border-navy-900');
            }

            if (isAnswered) {
                btn.classList.add('bg-blue-600', 'text-white', 'border-blue-700');
                answeredCount++;
            } else {
                btn.classList.add('bg-white', 'text-slate-700', 'border-slate-200');
            }

            if (isFlagged) {
                btn.classList.add('border-2', 'border-amber-500');
                flaggedCount++;
            }
        });

        // Update statistics counters
        statAnswered.textContent = answeredCount;
        statUnanswered.textContent = questions.length - answeredCount;
        statFlagged.textContent = flaggedCount;
        answeredCountBadge.textContent = `${answeredCount} / ${questions.length}`;
    }

    // Render a single question by index
    function renderQuestion(index) {
        if (index < 0 || index >= questions.length) return;
        currentIndex = index;
        const q = questions[index];

        currentQNum.textContent = index + 1;
        categoryText.textContent = getCategoryName(q.category_id);
        difficultyText.textContent = q.difficulty || 'Media';
        qText.textContent = q.question;

        // Render options text
        document.getElementById('opt-text-A').textContent = q.option_a;
        document.getElementById('opt-text-B').textContent = q.option_b;
        document.getElementById('opt-text-C').textContent = q.option_c;
        document.getElementById('opt-text-D').textContent = q.option_d;

        // Highlight selected option if already answered
        const selectedOpt = userAnswers[q.id];
        const optionCards = optionsContainer.querySelectorAll('.option-card');
        optionCards.forEach(card => {
            const opt = card.dataset.option;
            const indicator = card.querySelector('.opt-indicator');
            if (selectedOpt === opt) {
                card.classList.add('selected', 'border-blue-600', 'bg-blue-50/60');
                indicator.classList.remove('border-slate-300', 'text-slate-600', 'bg-white');
                indicator.classList.add('border-blue-600', 'bg-blue-600', 'text-white');
            } else {
                card.classList.remove('selected', 'border-blue-600', 'bg-blue-50/60');
                indicator.classList.remove('border-blue-600', 'bg-blue-600', 'text-white');
                indicator.classList.add('border-slate-300', 'text-slate-600', 'bg-white');
            }
        });

        // Update Flag button state
        if (flaggedQuestions.has(q.id)) {
            flagBtn.classList.add('bg-amber-50', 'border-amber-400', 'text-amber-800');
            flagText.textContent = 'Duda Marcada';
        } else {
            flagBtn.classList.remove('bg-amber-50', 'border-amber-400', 'text-amber-800');
            flagText.textContent = 'Marcar Duda';
        }

        // Prev / Next button states
        prevBtn.disabled = (currentIndex === 0);
        prevBtn.classList.toggle('opacity-50', currentIndex === 0);
        prevBtn.classList.toggle('cursor-not-allowed', currentIndex === 0);

        if (currentIndex === questions.length - 1) {
            nextBtn.innerHTML = `<span>Revisar Examen</span> <i data-lucide="check-circle" class="w-4 h-4"></i>`;
        } else {
            nextBtn.innerHTML = `<span>Siguiente</span> <i data-lucide="chevron-right" class="w-4 h-4"></i>`;
        }

        updatePalette();
        lucide.createIcons();
    }

    function getCategoryName(catId) {
        const map = {
            'notariado_puro': 'Ley de Notariado y Función Notarial',
            'jurisdiccion_voluntaria': 'Jurisdicción Voluntaria (LENJVOD)',
            'civil_sucesiones': 'Derecho Civil y Sucesiones',
            'familia_menores': 'Derecho de Familia y Menores',
            'mercantil_societario': 'Derecho Mercantil y Títulos Valores',
            'registral_cnr': 'Derecho Registral y Catastro (CNR)'
        };
        return map[catId] || catId;
    }

    const autoAdvanceToggle = document.getElementById('auto-advance-toggle');
    let autoAdvanceTimer = null;

    function selectOption(selectedOpt) {
        if (!questions || questions.length === 0) return;
        const currentQ = questions[currentIndex];
        userAnswers[currentQ.id] = selectedOpt;

        // Immediate visual feedback on selected card
        const optionCards = optionsContainer.querySelectorAll('.option-card');
        optionCards.forEach(card => {
            const opt = card.dataset.option;
            const indicator = card.querySelector('.opt-indicator');
            if (selectedOpt === opt) {
                card.classList.add('selected', 'border-blue-600', 'bg-blue-50/90', 'ring-2', 'ring-blue-500/20');
                indicator.classList.remove('border-slate-300', 'text-slate-700', 'bg-white');
                indicator.classList.add('border-blue-600', 'bg-blue-600', 'text-white');
            } else {
                card.classList.remove('selected', 'border-blue-600', 'bg-blue-50/90', 'ring-2', 'ring-blue-500/20');
                indicator.classList.remove('border-blue-600', 'bg-blue-600', 'text-white');
                indicator.classList.add('border-slate-300', 'text-slate-700', 'bg-white');
            }
        });

        updatePalette();

        // Auto-advance to next question if enabled
        if (autoAdvanceToggle && autoAdvanceToggle.checked) {
            clearTimeout(autoAdvanceTimer);
            if (currentIndex < questions.length - 1) {
                nextBtn.classList.add('ring-4', 'ring-blue-300');
                autoAdvanceTimer = setTimeout(() => {
                    nextBtn.classList.remove('ring-4', 'ring-blue-300');
                    renderQuestion(currentIndex + 1);
                }, 260);
            }
        }
    }

    // Select option handler on click
    optionsContainer.querySelectorAll('.option-card').forEach(card => {
        card.addEventListener('click', () => {
            selectOption(card.dataset.option);
        });
    });

    // Keyboard Shortcuts: 1-4, A-D, Arrow keys, Enter
    document.addEventListener('keydown', (e) => {
        if (confirmModal && !confirmModal.classList.contains('hidden')) return;
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        const key = e.key.toUpperCase();
        if (key === 'A' || key === '1') {
            e.preventDefault();
            selectOption('A');
        } else if (key === 'B' || key === '2') {
            e.preventDefault();
            selectOption('B');
        } else if (key === 'C' || key === '3') {
            e.preventDefault();
            selectOption('C');
        } else if (key === 'D' || key === '4') {
            e.preventDefault();
            selectOption('D');
        } else if (e.key === 'ArrowRight' || e.key === 'Enter') {
            e.preventDefault();
            if (currentIndex < questions.length - 1) {
                renderQuestion(currentIndex + 1);
            } else {
                openSubmitModal();
            }
        } else if (e.key === 'ArrowLeft') {
            e.preventDefault();
            if (currentIndex > 0) renderQuestion(currentIndex - 1);
        }
    });

    // Toggle Flag
    flagBtn.addEventListener('click', () => {
        const currentQ = questions[currentIndex];
        if (flaggedQuestions.has(currentQ.id)) {
            flaggedQuestions.delete(currentQ.id);
        } else {
            flaggedQuestions.add(currentQ.id);
        }
        renderQuestion(currentIndex);
    });

    // Navigation buttons
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) renderQuestion(currentIndex - 1);
    });

    nextBtn.addEventListener('click', () => {
        if (currentIndex < questions.length - 1) {
            renderQuestion(currentIndex + 1);
        } else {
            openSubmitModal();
        }
    });

    // Timer Countdown
    function startTimer() {
        timerInterval = setInterval(() => {
            timeRemaining--;
            if (timeRemaining <= 0) {
                clearInterval(timerInterval);
                timerDisplay.textContent = '00:00';
                autoSubmitExam();
                return;
            }

            const mins = Math.floor(timeRemaining / 60);
            const secs = timeRemaining % 60;
            timerDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

            // Visual warnings for low time
            if (timeRemaining <= 300 && timeRemaining > 120) {
                // < 5 mins (amber warning)
                timerBox.classList.remove('bg-slate-900');
                timerBox.classList.add('bg-amber-600');
            } else if (timeRemaining <= 120) {
                // < 2 mins (pulsing red warning)
                timerBox.classList.remove('bg-slate-900', 'bg-amber-600');
                timerBox.classList.add('bg-red-600', 'timer-warning');
            }
        }, 1000);
    }

    // Modal Confirm Submission
    function openSubmitModal() {
        const answeredCount = Object.keys(userAnswers).length;
        const unansweredCount = questions.length - answeredCount;

        modalAnsweredCount.textContent = answeredCount;
        if (unansweredCount > 0) {
            modalUnansweredWarning.classList.remove('hidden');
            modalUnansweredCount.textContent = unansweredCount;
        } else {
            modalUnansweredWarning.classList.add('hidden');
        }

        confirmModal.classList.remove('hidden');
    }

    modalCancelBtn.addEventListener('click', () => {
        confirmModal.classList.add('hidden');
    });

    finishBtn.addEventListener('click', () => {
        openSubmitModal();
    });

    modalConfirmBtn.addEventListener('click', () => {
        confirmModal.classList.add('hidden');
        submitExam();
    });

    async function autoSubmitExam() {
        alert('¡El tiempo oficial de 25 minutos ha finalizado! Su examen se enviará y calificará automáticamente.');
        submitExam();
    }

    async function submitExam() {
        if (isSubmitting) return;
        isSubmitting = true;
        clearInterval(timerInterval);

        const timeSpent = totalTimeSeconds - Math.max(0, timeRemaining);

        // Show loading in finish button
        finishBtn.innerHTML = `<i data-lucide="loader-2" class="w-4 h-4 animate-spin"></i> <span>Calificando...</span>`;
        lucide.createIcons();

        try {
            const res = await fetch('/api/exam/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    time_spent_seconds: timeSpent,
                    answers: userAnswers
                })
            });

            const data = await res.json();
            if (data.success && data.redirect_url) {
                window.location.href = data.redirect_url;
            } else {
                alert('Error al evaluar examen: ' + (data.error || 'Desconocido'));
                isSubmitting = false;
            }
        } catch (err) {
            console.error('Error submitting exam:', err);
            alert('Error al conectar con el servidor.');
            isSubmitting = false;
        }
    }

    // Expose AI Question helper in Exam Mode
    window.askCurrentExamQuestionToAI = function() {
        if (!questions || questions.length === 0 || currentIndex >= questions.length) return;
        const q = questions[currentIndex];
        const promptText = `Por favor analízame la siguiente pregunta de examen de notariado: "${q.question}". ¿Cuáles son las disposiciones legales de El Salvador aplicables y qué consideraciones doctrinales debo tener presentes para resolverla?`;
        
        if (typeof window.openAIAssistantWithContext === 'function') {
            window.openAIAssistantWithContext(promptText);
        } else {
            const drawer = document.getElementById('ai-assistant-drawer');
            const input = document.getElementById('ai-assistant-input');
            if (drawer && input) {
                drawer.classList.remove('hidden');
                input.value = promptText;
                if (typeof window.sendAIMessage === 'function') window.sendAIMessage();
            }
        }
    };

    // Start
    initExam();
});
