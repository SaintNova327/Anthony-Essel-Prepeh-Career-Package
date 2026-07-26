document.addEventListener("DOMContentLoaded", () => {

    const elements = document.querySelectorAll(
        "section, .card, .engineering-card, .gallery-card, .timeline-item"
    );

    const observer = new IntersectionObserver(entries => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    }, {

        threshold: 0.15

    });

    elements.forEach(el => {

        el.classList.add("hidden");

        observer.observe(el);

    });

});