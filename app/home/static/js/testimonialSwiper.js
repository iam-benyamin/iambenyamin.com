const testimonialsContainer = document.querySelector('.testimonials-container');
const testimonial = testimonialsContainer.querySelector('.testimonial');
const logo = testimonialsContainer.querySelector('.logo');
const username = testimonialsContainer.querySelector('.username');
const role = testimonialsContainer.querySelector('.role');

const api_url = `${window.location.href}testimonial/`;
let idx = 1;
let data = [];

async function getapi(url) {
    const response = await fetch(url);
    data = await response.json();
}
getapi(api_url);

function updateTestimonial() {
    let { name, job_position, profile_iamge, description } = data[idx];

    testimonial.innerHTML = description;
    logo.src = profile_iamge;
    username.innerHTML = name;
    role.innerHTML = job_position;

    idx++;
    if (idx > data.length - 1) {
        idx = 0;
    }
}

setInterval(updateTestimonial, 10000);