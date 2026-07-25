document.addEventListener("DOMContentLoaded",()=>{

    /* ===============================
       Scroll Animation
    =============================== */

    const elements=document.querySelectorAll(
        "section,.card,.engineering-card,.timeline-item,.gallery-item"
    );

    const observer=new IntersectionObserver((entries)=>{

        entries.forEach(entry=>{

            if(entry.isIntersecting){

                entry.target.classList.add("visible");

            }

        });

    },{

        threshold:.15

    });

    elements.forEach(el=>{

        el.classList.add("hidden");

        observer.observe(el);

    });

    /* ===============================
       Animated Counters
    =============================== */

    const counters=document.querySelectorAll(".stat-card h3");

    counters.forEach(counter=>{

        const value=counter.innerText;

        const number=parseInt(value);

        if(isNaN(number)) return;

        let count=0;

        const speed=Math.max(10,number/40);

        const timer=setInterval(()=>{

            count+=speed;

            if(count>=number){

                counter.innerText=value;

                clearInterval(timer);

            }else{

                counter.innerText=Math.floor(count);

            }

        },20);

    });

});