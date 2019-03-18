$(function () {

    var swiper1 = new Swiper('#swiper1', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        autoplay: 3000,
        loop: true
    });




    var swiper2 = new Swiper('#swiper2', {

        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 4,
        spaceBetween: 3,

        loop: true
    });


        var swiper3 = new Swiper('#swiper3', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        // autoplay: 3000,
        loop: true
    });






})