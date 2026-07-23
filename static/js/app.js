/* ===========================================
   VERITAS AI
   app.js
=========================================== */

document.addEventListener("DOMContentLoaded", () => {

    /* ===============================
       Character Counter
    =============================== */

    const textarea = document.getElementById("news");
    const counter = document.getElementById("charCount");

    if (textarea && counter) {

        const updateCounter = () => {
            counter.textContent = textarea.value.length;
        };

        textarea.addEventListener("input", updateCounter);
        updateCounter();
    }

    /* ===============================
       Model Card Selection
    =============================== */

    const modelCards = document.querySelectorAll(".model-card");

    modelCards.forEach(card => {

        card.addEventListener("click", () => {

            modelCards.forEach(c => c.classList.remove("selected"));

            card.classList.add("selected");

            const radio = card.querySelector("input");

            if (radio) {
                radio.checked = true;
            }

        });

    });

    /* ===============================
       Button Loading Animation
    =============================== */

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            const button = document.querySelector(".detect-btn");

            if (button) {

                button.disabled = true;

                button.innerHTML = `
                    <span class="spinner-border spinner-border-sm"></span>
                    Analyzing...
                `;

            }

        });

    }

    /* ===============================
       Fade In Animation
    =============================== */

    const fadeItems = document.querySelectorAll(".glass");

    fadeItems.forEach((item, index) => {

        item.style.opacity = "0";
        item.style.transform = "translateY(25px)";

        setTimeout(() => {

            item.style.transition = ".6s ease";

            item.style.opacity = "1";
            item.style.transform = "translateY(0px)";

        }, index * 150);

    });

    /* ===============================
       Navbar Active Link
    =============================== */

    const currentPage = window.location.pathname;

    document.querySelectorAll(".sidebar a").forEach(link => {

        link.classList.remove("active");

        if (link.getAttribute("href") === currentPage) {

            link.classList.add("active");

        }

    });

    /* ===============================
       Smooth Hover Effect
    =============================== */

    document.querySelectorAll(".glass").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-8px)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "translateY(0px)";

        });

    });

    /* ===============================
       Progress Bar Animation
    =============================== */

    const progress = document.querySelector(".progress-bar");

    if (progress) {

        const width = progress.style.width;

        progress.style.width = "0%";

        setTimeout(() => {

            progress.style.transition = "1.5s ease";

            progress.style.width = width;

        }, 300);

    }

    /* ===============================
       Floating Glow Animation
    =============================== */

    const glows = document.querySelectorAll(".background-glow");

    glows.forEach((glow, index) => {

        glow.animate(
            [
                {
                    transform: "translateY(0px)"
                },
                {
                    transform: "translateY(30px)"
                },
                {
                    transform: "translateY(0px)"
                }
            ],
            {
                duration: 7000 + (index * 1000),
                iterations: Infinity
            }
        );

    });

});