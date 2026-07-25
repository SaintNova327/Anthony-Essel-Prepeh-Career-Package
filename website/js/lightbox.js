document.addEventListener("DOMContentLoaded",()=>{

    const images=[...document.querySelectorAll(".lightbox-image")];

    if(images.length===0) return;

    let current=0;

    const overlay=document.createElement("div");

    overlay.id="lightbox-overlay";

    overlay.innerHTML=`

        <span id="lightbox-close">&times;</span>

        <button id="lightbox-prev">&#10094;</button>

        <img id="lightbox-image">

        <button id="lightbox-next">&#10095;</button>

        <div id="lightbox-counter"></div>

    `;

    document.body.appendChild(overlay);

    const img=document.getElementById("lightbox-image");

    const counter=document.getElementById("lightbox-counter");

    function show(index){

        current=index;

        img.src=images[current].src;

        counter.textContent=`${current+1} / ${images.length}`;

        overlay.classList.add("show");

    }

    images.forEach((image,index)=>{

        image.addEventListener("click",()=>{

            show(index);

        });

    });

    document.getElementById("lightbox-prev").onclick=()=>{

        current--;

        if(current<0) current=images.length-1;

        show(current);

    };

    document.getElementById("lightbox-next").onclick=()=>{

        current++;

        if(current>=images.length) current=0;

        show(current);

    };

    document.getElementById("lightbox-close").onclick=()=>{

        overlay.classList.remove("show");

    };

    overlay.onclick=(e)=>{

        if(e.target===overlay){

            overlay.classList.remove("show");

        }

    };

    document.addEventListener("keydown",(e)=>{

        if(!overlay.classList.contains("show")) return;

        if(e.key==="ArrowRight"){

            document.getElementById("lightbox-next").click();

        }

        if(e.key==="ArrowLeft"){

            document.getElementById("lightbox-prev").click();

        }

        if(e.key==="Escape"){

            overlay.classList.remove("show");

        }

    });

});