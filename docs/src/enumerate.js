window.addEventListener("load", function () {
  const hxArr = Array.from(document.querySelectorAll("[data-headerNum]"));

  enumerateHeader(hxArr);
});

const enumerateHeader = (headerList) => {
  headerList.forEach((hx) => {
    const tocChunk = document.createElement("div");
    const link = document.createElement("a");
    link.setAttribute("href", "#" + hx.id);
    link.innerHTML = hx.getAttribute("data-headerNum") + ". " + hx.innerHTML;
    tocChunk.appendChild(link);
    tocChunk.setAttribute("class", `tocChunk tocChunk-${hx.tagName.toLowerCase()}`);
    document.getElementsByClassName("sidebar")[0].appendChild(tocChunk);
  });
};
