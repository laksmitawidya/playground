// Javascript has 2 data types : Primitive and References

// var => function scoped, global variable, window object -> can be accessed everywhere
// es6 => let, const => blocked-scoped
// 1. PRIMITIVE
let name = 'Mita' //string
let age = 25 // number
let isApproved = true //boolean literal
let firstName // not defined -> undefined
let lastName = null // empty the variable, type of var : object
console.log("This Undefined variable is:", firstName)

// javascript is DYNAMIC TYPING -> all types are number, javascript doesn't have a float or integer
console.log("Type of variable :", typeof(name))


// 2. REFERENCES TYPE : object, array and function -> copy by reference, all variable & memory location also copied
// a. object
let person = {
    name,
    age
}
console.log("Person :", person, "Name :", person.name, "Age :", person.age)

// bracket notation
person['name'] = 'Marry'
person['age'] = 25

let selection = 'name'

console.log("Person :", person, "Name :", person['name'], "Age :", person['age'], person[selection])

// b. array notation -> is dynamic, type object has properties, inherited from somewhere place
let selectedColors = ['red', 'blue']
selectedColors.push('pink')
selectedColors.push(1)
console.log("Selected Colors:", selectedColors, selectedColors[0])

console.log(typeof(selectedColors))

console.log(selectedColors)


// c. function
function greet(names) {
    console.log("hello " + names)
}

let names = 'John'
greet(names)
greet("Marry")

// STRING
// template literal, will print excatly like what we want to type

const textTemplate =
    `Hi ${name} ${2+3}

Thank you for joining my mailing list

Regards,
Mita`
console.log(textTemplate)

// string has 2 types : primitive and object

let message = 'this is my first message'
let anotherMessage = new String('hi')

message.indexOf('my') // which index is it
message.length // how many length
message[0]
message.includes('not')
message.startsWith('this')
message.endsWith('e')
message.replace('first', 'second')
message.toUpperCase()
message.trim()
message.trimLeft()
message.trimRight()

// escape notation with the special character 
// /, \n, etc


// it will modify, but will not modify the original string because datatype in javascript is imutable


// value type 
// - immutable
// - reference is compared by memory location, value is compared by value
// ex : let a = {a, b, c} let b = {a, b, c} // returns false because it compares by the memory, not the value
// value types are copied by value
// ex : let x : 'apple', let y = x