// =========================
// Loading Screen Animation
// =========================

const launchBtn = document.getElementById("launchBtn");
const loadingScreen = document.getElementById("loadingScreen");
const progressBar = document.getElementById("progressBar");
const loadingText = document.getElementById("loadingText");

const steps = [
    "Initializing Security Console...",
    "Loading AI Model...",
    "Loading Random Forest...",
    "Loading Network Modules...",
    "Preparing Dashboard..."
];

launchBtn.addEventListener("click", () => {

    launchBtn.style.display = "none";

    loadingScreen.style.display = "block";

    let progress = 0;
    let step = 0;

    loadingText.innerHTML = steps[step];

    const interval = setInterval(() => {

        progress++;

        progressBar.style.width = progress + "%";

        // Change loading message every 20%
        if (progress % 20 === 0 && step < steps.length - 1) {

            step++;
            loadingText.innerHTML = steps[step];

        }

        // Finished
        if (progress >= 100) {

            clearInterval(interval);

            loadingText.innerHTML = "Launching Security Console...";

            setTimeout(() => {

                // Open Streamlit Dashboard
                window.location.href = "http://localhost:8501";

            }, 800);

        }

    }, 30);

});