// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
let linkTag = searchWrapper.querySelector("a");
let webLink;

// if user presses any key and releases
inputBox.oninput = (e) => {
    let userData = e.target.value; // user entered data
    let emptyArray = [];

    if (userData) {
        icon.onclick = () => {
            webLink = `https://www.google.com/search?q=${userData}`;
            linkTag.setAttribute("href", webLink);
            linkTag.click();
        }
        emptyArray = suggestions.filter((data) => {
            // filtering array value and user characters to lowercase and return only those words which start with user entered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data) => {
            // passing return data inside li tag
            return data = `<li>${data}</li>`;
        });
        showSuggestions(emptyArray);
    } else {
        hideSuggestions();
    }
}

function select(element) {
    let selectData = element.textContent;
    inputBox.value = selectData;
    icon.onclick = () => {
        webLink = `https://www.google.com/search?q=${selectData}`;
        linkTag.setAttribute("href", webLink);
        linkTag.click();
    }
    hideSuggestions();
}

function showSuggestions(list) {
    let listData;
    if (!list.length) {
        listData = "<li>No suggestions found</li>";
    } else {
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
    searchWrapper.classList.add("active"); // show autocomplete box
}

function hideSuggestions() {
    suggBox.innerHTML = "";
    searchWrapper.classList.remove("active"); // hide autocomplete box
}
