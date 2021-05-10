$(document).ready(function() {
    // 手机导航
    $('.menuBtn').append('<b></b><b></b><b></b>');
    $('.menuBtn').click(function(event) {
        $(this).toggleClass('open');
        $('.nav').stop().slideToggle();
    });

    var _winw = $(window).width();
    if (_winw > 959) {
        $('.nav li').hover(function() {
            $(this).find('.sub').stop().slideDown();
            if ($(this).find('.sub').length) {
                $(this).addClass('ok');
                // $('.header').addClass('on');
            } else {
                // $('.header').removeClass('on');
            }
        }, function() {
            $(this).removeClass('ok');
            $(this).find('.sub').stop().slideUp();
        });
        // $('.nav').mouseleave(function(event) {
        //     if ($('.header').hasClass('on')) {
        //         $('.header').removeClass('on');
        //     };
        // });
    } else {
        $('.nav .v1').click(function() {
            if ($(this).siblings('.sub').length) {
                $(this).parents('li').siblings('li').find('.sub').stop().slideUp();
                $(this).siblings('.sub').stop().slideToggle();
                return false;
            }
        });
    }


    // 选项卡 鼠标点击
    $(".TAB_CLICK li").click(function() {
        var tab = $(this).parent(".TAB_CLICK");
        var con = tab.attr("id");
        var on = tab.find("li").index(this);
        $(this).addClass('on').siblings(tab.find("li")).removeClass('on');
        $(con).eq(on).addClass('show').siblings(con).removeClass('show');
    });
    $('.TAB_CLICK').each(function(index, el) {
        if ($(this).find('li.on').length) {
            $(this).find("li.on").trigger('click');
        } else {
            $(this).find("li").filter(':first').trigger('click');
        }
    });

    // wow动画
    if (!(/msie [6|7|8|9]/i.test(navigator.userAgent))) {
        var wow = new WOW({
            boxClass: 'wow',
            animateClass: 'animated',
            offset: -100,
            mobile: false,
            live: true
        });
        wow.init();
    };

    // 头部
    // $('.nav>ul>li>.v1').mouseenter(function() {
    //  $(this).siblings('.sub').stop().slideDown();
    // })
    // $('.sub').mouseleave(function() {
    //  $(this).stop().slideUp();
    // })

    $('.header .so-btn').click(function() {
        $(this).toggleClass('on');
        if ($(this).hasClass('on')) {
            $(this).siblings('.form-so').stop().slideDown();
        } else {
            $(this).siblings('.form-so').stop().slideUp();
        }
    })
    $('.hd-close').click(function() {
        $('.box-so').stop().slideUp();
    })
    $('.menuBtn1').click(function() {
        $(this).toggleClass('open');
        $('.header .so-btn').siblings('.form-so').toggleClass('on');
        if ($(this).hasClass('open')) {
            $('.nav').css('display', 'none');
            $('.hd-r').addClass('open');
            $('.wp2').addClass('open');
            $('.navopen').stop().slideDown();
            $('.header .so-btn,.list01').css('display', 'none');
        } else {
            $('.nav').css('display', 'inline-block');
            $('.hd-r').removeClass('open');
            $('.wp2').removeClass('open');
            $('.navopen').stop().slideUp();
            $('.header .so-btn,.list01').css('display', 'block');
        }
    })
    $('.nav>ul>li').click(function() {
        $(this).toggleClass('on').siblings().removeClass('on');
    })


});