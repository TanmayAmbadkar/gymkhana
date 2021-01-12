function setPos(){

    window.scrollTo(0,parseInt(localStorage['position']));
}

document.getScroll = function() {
    if (window.pageYOffset != undefined) {
        return pageYOffset;
    } else {
        var sx, sy, d = document,
            r = d.documentElement,
            b = d.body;
        sx = r.scrollLeft || b.scrollLeft || 0;
        sy = r.scrollTop || b.scrollTop || 0;
        return sy;
    }
}

function getPos(){
    localStorage['position'] = document.getScroll()
}

// document.addEventListener("DOMContentLoaded", function() {
//   setPos()
//   localStorage['position'] = "0"
// });
