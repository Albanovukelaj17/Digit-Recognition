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