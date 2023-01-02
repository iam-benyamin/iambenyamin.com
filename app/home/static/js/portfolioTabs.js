
function togglePortfolioItem(event) {
    const tabButtons = document.querySelectorAll('#portfolio .content .row button');
    const portfolioCards = document.querySelectorAll("#portfolio .content .card-area .card");
    let dataFilter = event.target.getAttribute('data-filter');

    if (dataFilter === 'all-work') {
        for (let i = 0; i < portfolioCards.length; i++) {
            portfolioCards[i].style.display = 'block';
        }
    } else {
        for (let i = 0; i < portfolioCards.length; i++) {
            if (portfolioCards[i].getAttribute('data-filter') === dataFilter) {
                portfolioCards[i].style.display = 'block';
            } else {
                portfolioCards[i].style.display = 'none';
            }
        }
    }

    for (let i = 0; i < tabButtons.length; i++) {
        tabButtons[i].className = tabButtons[i].className.replace('active', '');
    }
    event.target.className += ' active';
}