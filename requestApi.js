// HTTP call in Ajax

const xhr = new XMLHttpRequest();
const url = 'https://jsonplaceholder.typicode.com/users';
xhr.open("GET", url);
xhr.send();
xhr.onreadystatechange = (e) => {
    //console.log(xhr.responseText)
}

// ajax jquery
$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url,
        success: function(result) {
            // console.log("result is :", result)
        }
    })
})

function makeAjaxCall(url, methodType, callback) {
    xhr.open(methodType, url, true)
    xhr.send()
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log("xhr done successfully")
                var response = xhr.responseText
                var respJson = JSON.parse(response)
                callback(respJson)
            } else {
                console.log("xhr failed")
            }
        } else {
            console.log("xhr processing going on")
        }
    }
    console.log("request sent successfully")
}

document.getElementById("userDetails").addEventListener("click", function() {
    var userId = document.getElementById('userId').value
    var URL = "https://api.github.com/users/" + userId
    makeAjaxCall(URL, "GET",
        processUserDetailsResponse)
})

document.getElementById("repoList").addEventListener("click", function() {
    // git hub url to get btford details
    var userId = document.getElementById("userId").value;
    var URL = "https://api.github.com/users/" + userId + "/repos";
    makeAjaxCall(URL, "GET", processRepoListResponse);
});

function processUserDetailsResponse(userData) {
    console.log("render user details", userData);
}

function processRepoListResponse(repoList) {
    console.log("render repo list", repoList);
}


//  Request api - React (error handling)
//  async - await
//  async componentDidMount() {
//     try {
//       const response = await fetch(`https://api.com/v1/ticker/?limit=10`);
//       const json = await response.json();
//       this.setState({ data: json });
//     } catch (error) {
//       console.log(error);
//     }
//   }


// Promise is used to overcome issues with multiple callbacks and provide better way to manage success and error conditions. Promise looks little complex in the beginning but its very simple and effective to deal with. Promise is an object which is returned by the async function like ajax. Promise object has three states

// pending :- means the async operation is going on.
// resovled :- async operation is completed successfully.
// rejected :- async operation is completed with error.


// Promise object is created.
// Async function returns the promise object
// If async is done successfully, promise object is resolved by calling its resolve method.
// If async is done with error, promise object is rejected by calling its rejected method.


// A cross-domain solution (CDS) is a means of information assurance that provides the ability to manually or automatically access or transfer information between two or more differing security domains.

//  Why do we need callback :- We need callback because we don’t want to duplicate the ajax code every time we need. We want to create a generic ajax function which takes ajax details as input along with callback reference. After completing the call, it calls the callback so that caller can resume with the result of the ajax call.
// What is callback :- Let’s say we have a function F1 which calls F2. F2 is doing some async operation like AJAX. F1 would like to know the result of the ajax call. Now F1 will pass another function say C1 as an additional parameter to F2 which F2 will call after it process the ajax request completely.