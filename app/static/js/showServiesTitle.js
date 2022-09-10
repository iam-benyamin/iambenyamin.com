const api_url = `${window.location.href}service-title/`;
let data = [];
const ul = document.querySelector("#footer > div > div > div.services > ul");
let li = "";


async function getapi(url) {
    const response = await fetch(url);
    data = await response.json();
    data.forEach(item => {
        li += `<li>${item.title}</li>`;
    })
    ul.innerHTML = li;
}
getapi(api_url);
