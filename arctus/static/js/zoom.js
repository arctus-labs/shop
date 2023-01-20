let img = document.getElementById('zoomjs');

img.addEventListener('mouseleave', function(e) {
    img.style.transform = '';
});

img.addEventListener('mousemove', function(e) {
    // only zoom if shift key is not pressed
    if (e.shiftKey) {
        img.style.transform = '';
        return;
    }

    let x = e.offsetX;
    let y = e.offsetY;
    let w = img.width;
    let h = img.height;
    let xP = (x / w) * 100;
    let yP = (y / h) * 100;
    img.style.transformOrigin = xP + '% ' + yP + '%';
    img.style.transform = 'scale(2)';
});
