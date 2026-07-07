async function loadSignals() {
    try {
        const res = await fetch("http://localhost:8000/signals");
        const data = await res.json();

        for (const ticker in data) {
            const row = document.getElementById(ticker);
            row.querySelector(".trend").innerText = data[ticker].trend;
            row.querySelector(".entry").innerText = data[ticker].entry ? "YES" : "NO";
            row.querySelector(".exit").innerText = data[ticker].exit ? "YES" : "NO";
        }
    } catch (err) {
        console.error("API error:", err);
    }
}

setInterval(loadSignals, 60000);
loadSignals();
