//Switch tabs on the home page
function switchTab(evt, tabName){
    var classes = document.getElementsByClassName('tab')
    switch (tabName) {
        case 'login':
        document.getElementById(tabName).style.display = "block";
        document.getElementById('signup').style.display = "none";
        classes[0].className = classes[0].className.replace(' active', '');
        classes[1].className+=' active';
            break;

        case 'signup':
        document.getElementById(tabName).style.display = "block";
        document.getElementById('login').style.display = "none";
        classes[1].className = classes[0].className.replace(' active', '');
        classes[0].className+=' active';
            break;

    }

}

function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}