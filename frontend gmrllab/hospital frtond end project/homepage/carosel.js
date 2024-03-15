$(document).ready(function () {
    $('.scroll').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 5,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 4000,

        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                arrows: false,
                slidesToShow: 4,
                slidesToScroll: 4,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 3,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                centerPadding: '0px',

            }
        }
        ]
    });
});

$(document).ready(function () {
    $('.package-scroll').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 3,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 3000,
        infinite: true,
        arrows: false,
        responsive: [
            {
                breakpoint: 1280,
                settings: {
                    arrows: false,
                    slidesToShow: 3,
                    slidesToScroll: 3,
                }
            },
            {
                breakpoint: 770,
                settings: {
                    arrows: false,
                    slidesToShow: 2,
                    slidesToScroll: 2,
                }
            },
            {
                breakpoint: 520,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2,
                    centerPadding: '0px',
                    dots: false,
                }
            }
        ]
    });
});
$(document).ready(function () {
    $('.main6_package-scroll').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 3,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 3000,
        infinite: true,
        arrows: false,
        responsive: [
            {
                breakpoint: 1280,
                settings: {
                    arrows: false,
                    slidesToShow: 3,
                    slidesToScroll: 3,
                }
            },
            {
                breakpoint: 770,
                settings: {
                    arrows: false,
                    slidesToShow: 2,
                    slidesToScroll: 2,
                }
            },
            {
                breakpoint: 520,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    centerPadding: '0px',

                }
            }
        ]
    });
});