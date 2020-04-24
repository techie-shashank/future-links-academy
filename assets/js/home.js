$(document).ready(function(){
    $('.navbar').removeClass('solid');
    $(window).scroll(function() {
        if($(this).scrollTop() > 50) {
            $('.navbar').addClass('solid');
        } else {
            $('.navbar').removeClass('solid');
        }
    });

    $('.text-carousel').slick({
        dots: true,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true
    });
    $('.tlt').textillate({
        in: {
            effect: 'tada'
        },
    });
});