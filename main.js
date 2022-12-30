//getting the pages
let mainCateories = document.querySelectorAll(".dropdown-menu");
mainCateories.forEach(function(el,i){
    el.querySelectorAll(".submenu-text").forEach(function(sel,si){
        console.log(sel.href);
    });
});

//cobasi
headings = document.evaluate("//button[contains(., 'Carregar mais produtos')]", document, null, XPathResult.ANY_TYPE, null );
thisHeading = headings.iterateNext();

var target = thisHeading;
// create an observer instance
var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        console.log(mutation.type);
    });
});

// configuration of the observer:
var config = { attributes: true, childList: true, characterData: true };

// pass in the target node, as well as the observer options
observer.observe(target, config);

// later, you can stop obse
observer.disconnect();


let d = document.getElementsByClassName("styles__MenuContent-sc-1t22uy7-4 busbto");
d = d[0];
d.querySelectorAll("li[class]");
