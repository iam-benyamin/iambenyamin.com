const servicesApiUrl = `/service-title/`;
let servicesData = [];
const ul = document.querySelector("#footer > div > div > div.services > ul");
let li = "";


async function getServiesAPI(url) {
    const response = await fetch(url);
    servicesData = await response.json();
    servicesData.forEach(item => {
        li += `<li>${item.title}</li>`;
    })
    ul.innerHTML = li;
}
getServiesAPI(servicesApiUrl);
