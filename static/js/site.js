const menu = document.querySelector(".menu");
const links = document.querySelector(".nav-links");

menu.addEventListener("click", () => {
  links.classList.toggle("open");
});

links.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => links.classList.remove("open"));
});
