function showTab(e, tabName) {
    var i, tabContent, tabBtn;
    tabContent = document.getElementsByClassName("about-tabs__content");
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }
    tabBtn = document.getElementsByClassName("nav-btn");
    for (i = 0; i < tabBtn.length; i++) {
        tabBtn[i].className = tabBtn[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    e.currentTarget.className += " active";
}

document.querySelector("#about-area .text-area .nav a:nth-child(1)").click()