// Lógica para las flashcards 3D de plazos notariales
document.addEventListener('DOMContentLoaded', () => {
    let cards = [];
    let currentIndex = 0;
    let isFlipped = false;
    let currentCategory = 'all';

    // DOM Elements
    const fcLoading = document.getElementById('fc-loading');
    const fcCardWrapper = document.getElementById('fc-card-wrapper');
    const fcCategoryLabel = document.getElementById('fc-category-label');
    const fcCurrentIndex = document.getElementById('fc-current-index');
    const fcTotalCount = document.getElementById('fc-total-count');
    const flashcardContainer = document.getElementById('flashcard-container');
    const cardInnerElement = document.getElementById('card-inner-element');
    const fcTitleFront = document.getElementById('fc-title-front');
    const fcPromptText = document.getElementById('fc-prompt-text');
    const fcArticleBack = document.getElementById('fc-article-back');
    const fcAnswerBack = document.getElementById('fc-answer-back');
    const fcPrevBtn = document.getElementById('fc-prev-btn');
    const fcNextBtn = document.getElementById('fc-next-btn');
    const fcFlipBtn = document.getElementById('fc-flip-btn');
    const catButtons = document.querySelectorAll('.fc-cat-btn');

    catButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            currentCategory = btn.dataset.cat;
            catButtons.forEach(b => {
                b.classList.remove('bg-amber-600', 'text-white');
                b.classList.add('bg-white', 'border', 'border-slate-200', 'text-slate-700');
            });
            btn.classList.add('bg-amber-600', 'text-white');
            btn.classList.remove('bg-white', 'border', 'border-slate-200', 'text-slate-700');

            loadCards(currentCategory);
        });
    });

    async function loadCards(cat) {
        fcLoading.classList.remove('hidden');
        fcCardWrapper.classList.add('hidden');
        currentIndex = 0;
        resetFlip();

        try {
            const res = await fetch(`/api/flashcards?category=${encodeURIComponent(cat)}`);
            const data = await res.json();
            if (data.success && data.flashcards.length > 0) {
                cards = data.flashcards;
                fcLoading.classList.add('hidden');
                fcCardWrapper.classList.remove('hidden');
                renderCard(0);
            } else {
                fcLoading.innerHTML = '<div class="text-slate-500 font-medium">No se encontraron fichas en esta categoría.</div>';
            }
        } catch (err) {
            console.error('Error fetching flashcards:', err);
            fcLoading.innerHTML = '<div class="text-rose-600 font-medium">Error al cargar las fichas.</div>';
        }
    }

    function renderCard(index) {
        if (index < 0 || index >= cards.length) return;
        currentIndex = index;
        resetFlip();

        const c = cards[index];
        fcCategoryLabel.textContent = c.category_name;
        fcCurrentIndex.textContent = index + 1;
        fcTotalCount.textContent = cards.length;

        fcTitleFront.textContent = c.title;
        fcPromptText.textContent = c.prompt;
        fcArticleBack.textContent = c.legal_article;
        fcAnswerBack.textContent = c.legal_answer;

        fcPrevBtn.disabled = (currentIndex === 0);
        fcPrevBtn.classList.toggle('opacity-50', currentIndex === 0);
        fcPrevBtn.classList.toggle('cursor-not-allowed', currentIndex === 0);

        lucide.createIcons();
    }

    function toggleFlip() {
        isFlipped = !isFlipped;
        flashcardContainer.classList.toggle('flipped', isFlipped);
    }

    function resetFlip() {
        isFlipped = false;
        flashcardContainer.classList.remove('flipped');
    }

    // Event listeners
    flashcardContainer.addEventListener('click', toggleFlip);
    fcFlipBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleFlip();
    });

    fcPrevBtn.addEventListener('click', () => {
        if (currentIndex > 0) renderCard(currentIndex - 1);
    });

    fcNextBtn.addEventListener('click', () => {
        if (currentIndex < cards.length - 1) {
            renderCard(currentIndex + 1);
        } else {
            // Loop back or message
            renderCard(0);
        }
    });

    // Spacebar to flip
    window.addEventListener('keydown', (e) => {
        if (e.code === 'Space' && !fcCardWrapper.classList.contains('hidden')) {
            e.preventDefault();
            toggleFlip();
        } else if (e.code === 'ArrowRight' && !fcCardWrapper.classList.contains('hidden')) {
            fcNextBtn.click();
        } else if (e.code === 'ArrowLeft' && !fcCardWrapper.classList.contains('hidden')) {
            fcPrevBtn.click();
        }
    });

    // Init
    loadCards(currentCategory);
});
