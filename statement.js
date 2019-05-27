// Conditional, if-else & switch case
let text;
let strawberry = document.getElementById("strawberry")
let apple = document.getElementById("apple")
let fruits = 'apple'
if (fruits === strawberry.value) {
    text = "How you like them strawberries ?";
} else if (fruits === apple.value) {
    text = "How you like them apples?";
} else {
    // last condtion
    text = "Banana is good!";
}

// 2. switch case
console.log("IF - else result is : " + text)


switch (fruits) {
    case "banana":
        text = "Banana is good!";
        break;
    case "orange":
        text = "I am not a fan of orange.";
        break;
    case "apple":
        text = "How you like them apples?";
        break;
    default:
        text = "I have never heard of that fruit...";
}
console.log("switch - case result is : " + text)

// STATEMENT
// break : Exits a switch or a loop
// const : Declares a variable with a constant value
// continue : Breaks one iteration (in the loop) if a specified condition occurs, and continues with the next iteration in the loop
// debugger	: Stops the execution of JavaScript, and calls (if available) the debugging function
// do ... while :	Executes a block of statements and repeats the block while a condition is true
// for :	Marks a block of statements to be executed as long as a condition is true
// for ... in :	Marks a block of statements to be executed for each element of an object (or array)
// function	: Declares a function
// if ... else ... else if :	Marks a block of statements to be executed depending on a condition
// let	: Declares a variable inside brackets {} scope
// return :	Stops the execution of a function and returns a value from that function
// switch :	Marks a block of statements to be executed depending on different cases
// throw :	Throws (generates) an error
// try ... catch ... finally :	Marks the block of statements to be executed when an error occurs in a try block, and implements error handling
// var : Declares a variable
// while : Marks a block of statements to be executed while a condition is true


// CALL BACK Function
// A callback is a function that is to be executed after another function has 
// finished executing — hence the name 'call back'. More complexly put: In JavaScript, 
// functions are objects. Because of this, functions can take functions as arguments,
//and can be returned by other functions.

// So why show you this? Because you can’t just call one 
// function after another and hope they execute in the right order. 
// Callbacks are a way to make sure certain code doesn’t execute 
// until other code has already finished execution.

// Example 1
function doHomework(subject, callback) {
    console.log(`Starting my ${subject} homework.`);
    callback()
}

let finish = function() { console.log('Finished my homework') }

doHomework('math', finish);

// Example 2
function first(callback) {
    // Simulate a code delay
    setTimeout(function() {
        console.log("Executed first");
    }, 500)
    callback()
}

let second = function() {
    console.log("Executed second");
}


first(second);