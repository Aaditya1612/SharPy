window.onscroll = function(){stickNav()};

function stickNav(){
    var navBar = document.getElementById('navbar');

    if(document.body.scrollTop > 80 || document.documentElement.scrollTop > 80){
        navBar.style.position ="fixed"
    }
}