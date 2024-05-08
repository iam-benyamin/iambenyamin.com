let btn = document.getElementById("to-top");

function showBtn() {
    let positionY = window.scrollY;
    if (positionY > 300) {
        btn.classList.add('show')
    } else {
        btn.classList.remove('show')
    }
};

function goToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' })
}

window.addEventListener('scroll', showBtn);
