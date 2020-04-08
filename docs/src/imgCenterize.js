window.addEventListener("load", function () {
  const imgs = Array.from(document.getElementsByTagName("img"));
  imgs.forEach((img) => {
    img.parentElement.classList.add("imgParent");
  });
});
