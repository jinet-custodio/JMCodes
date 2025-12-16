//for viewing certificates
const imageModal = document.getElementById("imageModal");
imageModal.addEventListener("show.bs.modal", function (event) {
    const button = event.relatedTarget;
    const imgSrc = button.getAttribute("data-img");

    const modalImage = document.getElementById("modalImage");
    modalImage.src = imgSrc;
});

//for sliding across certs
function scrollSlider(direction) {
    const slider = document.getElementById("certSlider");
    const scrollAmount = 300; // pixels per click
    slider.scrollLeft += direction * scrollAmount;
}

document.addEventListener("DOMContentLoaded", (event) => {
    const allBtn = document.getElementById('allCerts');
    const pyBtn = document.getElementById('pythonCerts');
    const opSysBtn = document.getElementById('opSysCerts');
    const cybersecBtn = document.getElementById('cybersecCerts');
    const others = document.getElementById('other');
    const allCerts = document.querySelectorAll('.cert');
    const pyCerts = document.querySelectorAll('.pythonCert');
    const opSysCerts = document.querySelectorAll('.OSCert');
    const cybersecCerts = document.querySelectorAll('.cybersecCert');
    const otherCerts = document.querySelectorAll('.others');

    function hideall() {
        allCerts.forEach((btn) => {
            btn.style.display = 'none';
        });
    }

    allBtn.addEventListener("click", (event) => {
        hideall();
        allCerts.forEach((btn) => {
            btn.style.display = 'block';
        });
    });

    pyBtn.addEventListener("click", (event) => {
        hideall();
        pyCerts.forEach((pyCert) => {
            pyCert.style.display = 'block';
        });
    });

    opSysBtn.addEventListener("click", (event) => {
        hideall();
        opSysCerts.forEach((OSCert) => {
            OSCert.style.display = 'block';
        });
    });

    cybersecBtn.addEventListener("click", (event) => {
        hideall();
        cybersecCerts.forEach((CSCert) => {
            CSCert.style.display = 'block';
        });
    });

    others.addEventListener("click", (event) => {
        hideall();
        otherCerts.forEach((OCert) => {
            OCert.style.display = 'block';
        });
    });



})
