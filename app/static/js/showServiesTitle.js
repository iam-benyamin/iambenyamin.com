const servicesApiUrl = `${window.location.host}/service-title/`;
let servicesData = [];
const ul = document.querySelector("#footer > div > div > div.services > ul");
let li = "";


async function getapi(url) {
    const response = await fetch(url);
    servicesData = await response.json();
    servicesData.forEach(item => {
        li += `<li>${item.title}</li>`;
    })
    ul.innerHTML = li;
}
getapi(servicesApiUrl);
