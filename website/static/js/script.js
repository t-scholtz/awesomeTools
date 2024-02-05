// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
let linkTag = searchWrapper.querySelector("a");
let webLink;

// if user presses any key and releases
inputBox.oninput = (e) => {
    let userData = e.target.value.trim(); // user entered data
    let emptyArray = [];

    if (userData) {
        emptyArray = suggestions.filter((item) => {
            // Filtering suggestions based on user input
            return item.text.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });

        // Convert HTML strings to DOM elements
        emptyArray = emptyArray.map((item) => {
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = `<li data-url="${item.url}" data-info="${item.info}">${item.text}</li>`;
            return tempDiv.firstElementChild;
        });

        // Create objects for the suggestions
        emptyArray = emptyArray.map((item) => {
            return { text: item.innerHTML, url: item.getAttribute('data-url'), info: item.getAttribute('data-info') };
        });

        console.log("emptyArray:", emptyArray); // Log the content of emptyArray

        showSuggestions(emptyArray);
    } else {
        hideSuggestions();
    }
};



function select(element) {
    let selectData = element.textContent;
    inputBox.value = selectData;
    search();
}


function search() {
    let searchData = inputBox.value.trim();
    if (searchData) {
        webLink = `https://www.google.com/search?q=${searchData}`;
        linkTag.setAttribute("href", webLink);
        linkTag.click();
    }
    hideSuggestions();
}


function showSuggestions(list) {
    console.log("list:", list); 
    let listData;
    if (!list.length) {
        listData = "<li>No suggestions found</li>";
    } else {
        listData = "";
        for (let i = 0; i < list.length; i++) {
            const item = list[i];
            console.log("item.text:", item.text); // Log the text property
            console.log("item.url:", item.url);   // Log the url property
            listData += `<li data-url="${item.url}" data-info="${item.info}">${item.text}</li>`;
        }
    }
    suggBox.innerHTML = listData;

    // Attach click event listeners to each suggestion
    const suggestionItems = suggBox.querySelectorAll('li');
    suggestionItems.forEach((item) => {
        item.addEventListener('click', () => {
            // Check if the selected item is not "No suggestions found"
            if (item.textContent !== "No suggestions found") {
                // Fill the input box with the selected suggestion and info
                inputBox.value = item.textContent + ' - ' + item.getAttribute('data-info');

                // Redirect to the corresponding URL
                window.location.href = item.getAttribute('data-url');
            }
        });
    });

    searchWrapper.classList.add("active"); // show autocomplete box
}

function hideSuggestions() {
    suggBox.innerHTML = "";
    searchWrapper.classList.remove("active"); // hide autocomplete box
}
