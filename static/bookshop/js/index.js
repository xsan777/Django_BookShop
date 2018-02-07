window.onload = function () {
    var mySwiper = new Swiper('.swiper-container', {
        // direction: 'horizontal',
        loop: true,
        speed: 300,
        autoplay: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },


    })
}

