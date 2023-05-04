let canvas = document.getElementById("canvas");
let context = canvas.getContext("2d");

let painting = false;

function startPosition(event) {
    painting = true;
    draw(event);
}

function finishedPosition() {
    painting = false;
    context.beginPath();
}

function draw(event) {
    if (!painting) return;
    context.lineWidth = 10;
    context.lineCap = "round";
    context.lineTo(event.clientX, event.clientY);
    context.stroke();
    context.beginPath();
    context.moveTo(event.clientX, event.clientY);
}

canvas.addEventListener("mousedown", startPosition);
canvas.addEventListener("mouseup", finishedPosition);
canvas.addEventListener("mousemove", draw);
