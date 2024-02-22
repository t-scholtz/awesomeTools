const searchWrapper = document.getElementById("searchWrapper");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
let linkTag = searchWrapper.querySelector("a");

let webLink;

inputBox.oninput = (e) => {
    let userData = e.target.value.trim().toLowerCase();// user entered data
    let emptyArray = [];

    if (userData) {
        emptyArray = suggestions.filter((item) => {
            // Filtering suggestions based on user input
            return item.text.toLocaleLowerCase().startsWith(userData);
        });

        if (emptyArray.length === 0) {
            emptyArray = suggestions.filter((item) => {
                // Filtering suggestions based on user input at the beginning of the suggestion text
                return item.text.toLowerCase().includes(userData);
            });
        }

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

inputBox.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        search();
    }
});

function search() {
    let searchData = inputBox.value.trim();
    if (searchData) {
        // Redirect to the search page with the search query as a parameter
        window.location.href = `/search?q=${encodeURIComponent(searchData)}`;
    }
    hideSuggestions();
}


function showSuggestions(list) {
    let listData;
    if (!list.length) {
        listData = "<li>No suggestions found</li>";
    } else {
        listData = "";
        for (let i = 0; i < list.length; i++) {
            const item = list[i];
            listData += `<li data-url="${item.url}" >${item.text}</li>`;
        }
    }
    suggBox.innerHTML = listData;

    // Attach click event listeners to each suggestion
    const suggestionItems = suggBox.querySelectorAll('li');
    suggestionItems.forEach((item) => {
        item.addEventListener('click', () => {
            // Check if the selected item is not "No suggestions found"
            if (item.textContent !== "No suggestions found") {
                inputBox.value = item.textContent;
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
