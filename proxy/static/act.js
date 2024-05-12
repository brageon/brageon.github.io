function updateCounter() {
    let count = parseInt(localStorage.getItem("visitorCount")) || 0;
    count++;
    localStorage.setItem("visitorCount", count);
    document.getElementById("counter").textContent = count; }
  window.onload = updateCounter;
