document.addEventListener("DOMContentLoaded", () => {

    const links = document.querySelectorAll(".lightbox");

    if (!links.length) return;

    // Create overlay
    const overlay = document.createElement("div");
    overlay.id = "lightbox-overlay";

    overlay.innerHTML = `
        <span id="lightbox-close">&times;</span>
        <img id="lightbox-image" src="" alt="">
    `;

    document.body.appendChild(overlay);

    const image = document.getElementById("lightbox-image");
    const close = document.getElementById("lightbox-close");

    links.forEach(link => {

        link.addEventListener("click", e => {

            e.preventDefault();

            image.src = link.href;

            overlay.classList.add("show");

        });

    });

    function hideLightbox(){

        overlay.classList.remove("show");

        image.src = "";

    }

    close.addEventListener("click", hideLightbox);

    overlay.addEventListener("click", e => {

        if(e.target === overlay){

            hideLightbox();

        }

    });

    document.addEventListener("keydown", e => {

        if(e.key === "Escape"){

            hideLightbox();

        }

    });

});