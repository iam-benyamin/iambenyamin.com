const testimonialsContainer = document.querySelector('.testimonials-container');
const testimonial = testimonialsContainer.querySelector('.testimonial');
const logo = testimonialsContainer.querySelector('.logo');
const username = testimonialsContainer.querySelector('.username');
const role = testimonialsContainer.querySelector('.role');

const TestimonialApiUrl = `${window.location.href}testimonial/`;
let idx = 1;
let testimonialsData = [];

async function getapi(url) {
    const response = await fetch(url);
    testimonialsData = await response.json();
}
getapi(TestimonialApiUrl);

function updateTestimonial() {
    let { name, job_position, profile_iamge, description } = testimonialsData[idx];

    testimonial.innerHTML = description;
    logo.src = profile_iamge;
    username.innerHTML = name;
    role.innerHTML = job_position;

    idx++;
    if (idx > testimonialsData.length - 1) {
        idx = 0;
    }
}

setInterval(updateTestimonial, 10000);