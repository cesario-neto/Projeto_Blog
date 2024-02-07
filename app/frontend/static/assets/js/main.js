const menuButton = document.querySelector(".mobile__menu");

menuButton.addEventListener("click", (e) => {
  const menu = document.querySelector(".mobile__menu__nav");
  menu.classList.toggle("mobile__menu__nav-animation");
});
