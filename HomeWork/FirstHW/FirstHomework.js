/* Устанавливает индекс слайда по умолчанию */
let slideIndex = 1;
showSlides(slideIndex);

/* Увеличивает индекс на 1 — показывает следующий слайд*/
function nextSlide() {
    showSlides(slideIndex += 1);
}

/* Уменьшает индекс на 1 — показывает предыдущий слайд*/
function previousSlide() {
    showSlides(slideIndex -= 1);
}

/* Устанавливается текущий слайд */
function currentSlide(n) {
    showSlides(slideIndex = n);
}

/* Функция перелистывания */
function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("item");

    if (n > slides.length) {
      slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }

  /* Прохожусь по каждому слайду  */
    for (let slide of slides) {
        slide.style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}

function alerted(){
  alert("Согласна, наша группа класс");
}


