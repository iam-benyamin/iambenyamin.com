const a = document.querySelectorAll('#header .menu ul li a');
const section = document.querySelectorAll('.section');

function ActivateMenu() {
    let current = '';
    section.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (sectionTop - (sectionHeight / 5) <= scrollY && scrollY <= (sectionTop + sectionHeight)) {
            current = section.getAttribute('id');
        }
    })
    a.forEach(item => {
        item.classList.remove('active');
        if (item.innerHTML.toLowerCase() == current) {
            item.classList.add('active');
        }
        if (current == 'header' || current == 'hero') {
            a[0].classList.add('active')
        }
    })
}

window.addEventListener('scroll', ActivateMenu)