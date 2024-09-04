let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');
let drawing = false;
//ctx.beginPath();
//ctx.moveTo(50, 50);
//ctx.lineTo(200, 200);
//ctx.stroke();
//test draw

canvas.addEventListener('mousedown', function(e) {
            drawing = true;ctx.beginPath();ctx.moveTo(e.offsetX, e.offsetY);
});

canvas.addEventListener('mousemove', function(e) {
    if (drawing){
        ctx.lineTo(e.offsetX, e.offsetY);  ctx.strokeStyle = "black";
        ctx.lineWidth = 10;ctx.lineCap = 'round';ctx.stroke();
    }
});
canvas.addEventListener('mouseup', function(e) {
            drawing = false;
});
canvas.addEventListener('mouseleave', function() {
    drawing = false;
}); // falls man aus den canvas raus geht ist gelcihgultig wie aufhören zu clicken
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}


function submitCanvas() {

    let dataURL = canvas.toDataURL('image/png');

    fetch('/submit_canvas', {
        method: 'POST',
        body: JSON.stringify({ image: dataURL }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert('Predicted digit: ' + data.prediction);
    });
}