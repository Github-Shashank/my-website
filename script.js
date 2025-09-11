const toggleButton = document.getElementById("darkModeToggle");

toggleButton.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");

  if (document.body.classList.contains("dark-mode")) {
    toggleButton.textContent = "☀️ Light Mode";
  } else {
    toggleButton.textContent = "🌙 Dark Mode";
  }
});
