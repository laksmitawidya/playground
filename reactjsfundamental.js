function sayHello() {
    for (let i = 0; i < 5; i++) {
        console.log(i)
    }
}

// var -> function
// let -> only when assign variable
// const -> can't be changed

const person2 = {
    name: 'Mosh',
    walk() {
        console.log(this)
    },

}
console.log("test")
person2.walk()
const walk = person2.walk
walk() 

// result = undefined because it's reference to window object

// BIND : function in js is object, has property and method. Bind method can set value this value, this here is based on the params that we send
// const doWalk = person.walk.bind(this)
// doWalk()

const square = function(number) {
    return number * number
}

const square2 = number => number * number
console.log(square2(5))

const jobs = [
    { id: 1, isActive: true },
    { id: 2, isActive: true },
    { id: 3, isActive: false },
    { id: 4, isActive: true },
]

const activeJobs = jobs.filter(function(job) { return job.isActive })
const activeJobs2 = jobs.filter(job => job.isActive)

// arrow function don't rebind the 'this' keyword

const restaurant = {
    getFood() {
        // this is a callback function -> return global object, solution create var self = this, it will reference to this
        setTimeout(function() {
                console.log("this 1:", this)
            })
            // arrow function don't rebind the 'this' keyword 
        setTimeout(() => {
            console.log("this 2:", this)
        })
    }
}
restaurant.getFood()

// Array Map
const colors = ['red', 'green', 'blue']


let colorsMap = colors.map((color) => {
    return color
})

console.log("colors Map:", colorsMap)

// object destructing
// const { id, isActive } = person
// or
// const { id, isActive: activate } = person

// spread operator
const fNumber = [1, 2, 3, ]
const sNumber = [4, 5, 6]
const clone = [...fNumber]
const combined1 = fNumber.concat(sNumber)
const combined2 = [...fNumber, 'a', ...sNumber]

console.log("Combined :", combined1, combined2, clone)

// clases
class Persona {
    constructor(name) {
        this.name = name
    }
    walk() {
        console.log("walkingggg")
    }
}

const persona = new Persona('Mosh')
persona.walk()

//inheritance 
class Teacher extends Persona {
    constructor(name, degree) {
        super()
        this.degree = degree
    }
    teach() {
        console.log("teachhhhhh")
    }
}


const teacher = new Teacher('Mosh', 'S1')
console.log("teacher: ", teacher.degree, teacher.name)

// if class put in a different file, should be using export 

// and how to import -> import { Person } from './teacher'
// const teacher = new Teacher("Mosh", "MSc")

// we can import one or more modules -> can be function or class, as long as has an export function
// class is an object
// export default -> we don't need a curly braches to import and only 1 single object that we want to import 

// Default -> import .. from ''
// Named -> { ... } from ''


// WHAT IS REACT?
// js library
// show content html to users and handle user interaction

// React can work by himself but need another library
// class -> React component are made by function or classes
// es 2015 syntax
// instance

// HTML looking stuf: JSX : special dialect to tell the js what the component look like
// that shows up in screen -> normal html (looks like html can be placed in js code, determines content of react app)


//Handle Reaction -> an event hadler
// user interaction and respond it using click, without, responing user 

// REACT SPLIT INTO 2 :
// React & react dom
// 1. React -> knows what component is and how to make component work togtether
// 2. ReactDom -> knows how to take a component and make it show up in the DOm using html
// 


// 1. npm : node package manager -> to install package in local
// 2. install
// 3. -g run package globally
// 4. name of package that we want to install


// app holding current state and component


