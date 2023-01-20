function buyNow() {
    productId = document.getElementById('product-id').value;

    // send request
    var request = new XMLHttpRequest();
    request.open('POST', '/api/buy-now', true);
    request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    request.send(JSON.stringify({productId: productId}));
}
