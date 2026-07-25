document.addEventListener("DOMContentLoaded", () => {

    const toggle = document.getElementById("theme-toggle");

    const body = document.body;

    const savedTheme = localStorage.getItem("theme");

    if(savedTheme === "dark"){

        body.classList.add("dark-theme");

    }

    updateIcon();

    if(toggle){

        toggle.addEventListener("click", ()=>{

            body.classList.toggle("dark-theme");

            localStorage.setItem(
                "theme",
                body.classList.contains("dark-theme")
                    ? "dark"
                    : "light"
            );

            updateIcon();

        });

    }

    function updateIcon(){

        if(!toggle) return;

        toggle.textContent =
            body.classList.contains("dark-theme")
            ? "☀️"
            : "🌙";

    }

});