//for viewing certificates
const imageModal = document.getElementById("imageModal");
imageModal.addEventListener("show.bs.modal", function (event) {
    const button = event.relatedTarget;
    const imgSrc = button.getAttribute("data-img");

    const modalImage = document.getElementById("modalImage");
    modalImage.src = imgSrc;
});
