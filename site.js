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

const beforeElement = document.getElementById("before_anim");
const afterElement = document.getElementById("after_anim");

beforeElement.addEventListener("animationend", () => {
  // 1. Hide the old element completely
  beforeElement.style.display = "none";
  
  // 2. Bring the new element into layout so it can animate
  afterElement.style.display = "block";
  
  // 3. Trigger the animation immediately
  afterElement.style.animation = "afterDriveUseTextAnim 0.5s forwards";
});


function typewriter(el) {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return; // show the full text
  const text = el.textContent;
  el.setAttribute('aria-label', text);          // screen readers get the full title at once
  el.textContent = '';
  const typed = document.createElement('span');
  const caret = document.createElement('span');
  const rest  = document.createElement('span');
  caret.className = 'tw-caret';
  rest.className  = 'tw-rest';
  el.append(typed, caret, rest);

  let i = 0;
  (function step() {
    typed.textContent = text.slice(0, i);
    rest.textContent  = text.slice(i);
    if (i === text.length) {
      setTimeout(() => caret.remove(), 2000);   // drop the caret after a pause (optional)
      return;
    }
    const prev = text[i - 1];
    i++;
    // short pause after punctuation, slightly random speed otherwise
    setTimeout(step, prev === '.' || prev === ',' ? 250 : 30 + Math.random() * 35);
  })();
}
setTimeout(() => document.querySelectorAll('[data-typewriter]').forEach(typewriter), 400);