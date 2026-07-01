// =============================
// Matrix Rain Animation
// =============================

const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

resizeCanvas();
window.addEventListener("resize", resizeCanvas);

// Characters
const characters =
"アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// Convert string to array
const chars = characters.split("");

// Font size
const fontSize = 18;

// Number of columns
let columns = Math.floor(canvas.width / fontSize);

// Y position of every drop
let drops = [];

function resetDrops() {
    columns = Math.floor(canvas.width / fontSize);
    drops = [];

    for (let i = 0; i < columns; i++) {
        drops[i] = Math.random() * -100;
    }
}

resetDrops();

window.addEventListener("resize", () => {
    resizeCanvas();
    resetDrops();
});

// Draw animation
function draw() {

    // Fade previous frame
    ctx.fillStyle = "rgba(5,7,13,0.08)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#00ff41";
    ctx.font = fontSize + "px monospace";

    for (let i = 0; i < drops.length; i++) {

        const text =
            chars[Math.floor(Math.random() * chars.length)];

        const x = i * fontSize;
        const y = drops[i] * fontSize;

        ctx.fillText(text, x, y);

        // Reset drop when it reaches bottom
        if (
            y > canvas.height &&
            Math.random() > 0.975
        ) {
            drops[i] = -20;
        }

        drops[i]++;

    }

}

setInterval(draw, 35);