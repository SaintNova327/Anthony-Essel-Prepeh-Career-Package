/*
============================================================
Anthony Essel Prepeh Portfolio
Main JavaScript
============================================================
*/

document.addEventListener("DOMContentLoaded", () => {

    console.log("Portfolio Loaded");

    /* ==========================================
       Mobile Navigation
    ========================================== */

    const menuButton = document.querySelector(".menu-toggle");
    const navigation = document.querySelector("nav");

    if (menuButton && navigation) {

        menuButton.addEventListener("click", () => {

            navigation.classList.toggle("active");

        });

    }

    /* ==========================================
       Smooth Scroll
    ========================================== */

    document.querySelectorAll('a[href^="#"]').forEach(link => {

        link.addEventListener("click", function(e){

            const target = document.querySelector(this.getAttribute("href"));

            if(target){

                e.preventDefault();

                target.scrollIntoView({

                    behavior:"smooth"

                });

            }

        });

    });

    /* ==========================================
       Scroll To Top
    ========================================== */

    const topButton = document.getElementById("topButton");

    if(topButton){

        window.addEventListener("scroll", () => {

            if(window.scrollY > 300){

                topButton.style.display = "block";

            }

            else{

                topButton.style.display = "none";

            }

        });

        topButton.addEventListener("click", () => {

            window.scrollTo({

                top:0,

                behavior:"smooth"

            });

        });

    }

});