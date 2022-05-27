let videoElement = document.querySelector('#video-style');
let playBtn = document.querySelector('.play-btn');

function playVideo() {
    playBtn.style.display = "none"
    videoElement.setAttribute('controls', '')
    videoElement.play();
}

function showPlayBtnAtEnded() {
    playBtn.style.display = 'block';
    videoElement.removeAttribute('controls')
}

videoElement.addEventListener('ended', showPlayBtnAtEnded);