const slider = document.getElementById("compare-slider");

if (slider) {

    const overlay = document.querySelector(".compare-overlay");

    slider.addEventListener("input", () => {

        overlay.style.width = slider.value + "%";

    });

}