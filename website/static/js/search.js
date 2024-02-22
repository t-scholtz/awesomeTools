const searchArea = document.getElementById("searchArea");
const inputArea = searchArea.querySelector("input");
const suggestionBox = document.getElementById("searchResultsContainer");

inputArea.oninput = (e) => {
    let userData = e.target.value.trim().toLowerCase();
    console.log("detected Change");
    console.log(userData);

    if (userData) {
        let filteredSuggestions = suggestions.filter((item) => {
            return item.text.toLowerCase().startsWith(userData);
        });
    
        let otherSuggestions = suggestions.filter((item) => {
            return item.text.toLowerCase().includes(userData) && !item.text.toLowerCase().startsWith(userData);
        });
    
        // Combine the suggestions with the starting query first, followed by other relevant suggestions
        let emptySet = new Set([...filteredSuggestions, ...otherSuggestions]);
    
        displaySuggestions(emptySet);
    }
    else{
        suggestionBox.innerHTML ="";
    }
};

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('q');
    if (searchQuery) {
        document.getElementById('searchBar2').value = searchQuery;
    }
    whenLoaded();
};

function whenLoaded(){
    let userData = inputArea.value.trim().toLowerCase();
    console.log("loaded ");
    console.log(userData);

    if (userData) {
        let filteredSuggestions = suggestions.filter((item) => {
            return item.text.toLowerCase().startsWith(userData);
        });
    
        let otherSuggestions = suggestions.filter((item) => {
            return item.text.toLowerCase().includes(userData) && !item.text.toLowerCase().startsWith(userData);
        });
    
        // Combine the suggestions with the starting query first, followed by other relevant suggestions
        let emptySet = new Set([...filteredSuggestions, ...otherSuggestions]);
    

        displaySuggestions(emptySet);
    } else {
        suggestionBox.innerHTML = "";
    }
}

function displaySuggestions(set) {
    let listData;
    let list =  [...set]; 
    if (!list.length) {
        listData = `<div class="box"><p class="title">No Suggestions Found</p><p class="subtitle">Try using a shorter and simpler search query <i class="fa fa-smile-o"></i></p></div>`;
    } else {
        listData = "";
        for (let i = 0; i < list.length; i++) {
            const item = list[i];
            listData += `<div class="box"><a href="${item.url}"><p class="title">${item.text}</p><p class="subtitle">${item.info}</p></a></div>`;
        }
    }
    suggestionBox.innerHTML = listData;

    const suggestionItems = suggestionBox.querySelectorAll('.box');
    suggestionItems.forEach((item) => {
        item.addEventListener('click', () => {
            inputArea.value = item.textContent;
            window.location.href = item.querySelector('a').getAttribute('href');
        });
    });

    searchArea.classList.add("active");
}

