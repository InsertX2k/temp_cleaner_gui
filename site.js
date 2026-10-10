// Fills in every <a data-link="key"> from the LINKS list in links.js
function applyLinks() {
  document.querySelectorAll('a[data-link]').forEach(a => {
    const url = LINKS[a.dataset.link];
    if (url) a.href = url;
    else console.warn('No entry in links.js for:', a.dataset.link);
  });
}
function include(file, pos) {
  return fetch(file).then(r => r.text()).then(html => {
    document.body.insertAdjacentHTML(pos, html);
    applyLinks();
    const here = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('nav a').forEach(a => {
      if (a.getAttribute('href') === here) a.setAttribute('aria-current', 'page');
    });
  });
}
applyLinks();
include('header.html', 'afterbegin');
include('footer.html', 'beforeend');
const lb = document.getElementById('lb');
if (lb) {
  document.querySelectorAll('.shots img').forEach(img =>
    img.addEventListener('click', () => { lb.querySelector('img').src = img.src; lb.showModal(); }));
  lb.addEventListener('click', () => lb.close());
}

const sups = document.getElementsByTagName('sup');
Array.from(sups).forEach(element => {
  const fi = element.children[0].href.indexOf('#');
  const elemid = element.children[0].href.substring(fi+1);
  element.addEventListener('click', () => {
    console.log(elemid);
    document.getElementById(elemid).style.transition = "background-color 2s ease-in-out";
    document.getElementById(elemid).style.backgroundColor = "rgba(217, 255, 3, 0.36)";
    setTimeout(() => {
      document.getElementById(elemid).style.backgroundColor = "rgba(217,255,3,0)";
    }, 3000);
  })
});

