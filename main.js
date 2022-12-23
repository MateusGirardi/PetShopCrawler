//getting the pages
let mainCateories = document.querySelectorAll(".dropdown-menu");
mainCateories.forEach(function(el,i){
    el.querySelectorAll(".submenu-text").forEach(function(sel,si){
        console.log(sel.href);
    });
});