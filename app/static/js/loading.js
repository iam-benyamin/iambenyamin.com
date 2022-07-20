
function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}

function turnOffLoading() {
    delay(1000).then(() => {
        var loading = document.getElementById('loading');
        loading.style.display = 'none';
    });
}

document.addEventListener('DOMContentLoaded', turnOffLoading);