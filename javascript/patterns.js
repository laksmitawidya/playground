// PATTERNS : factory vs constructor 
function createCircle(radius) {
    return circle = {
        radius,
        draw() {
            console.log('draw')
        }
    }
}

const circle1 = createCircle(1)
console.log(circle1)

const circle2 = createCircle(2)
console.log(circle2)

// Constructor Function
function Circle(radius) {
    this.radius = radius
    this.draw = function() {
        console.log('draw')
    }
}

// 1. create empty object
// 2. set circle to object
// 3. assign to object

//  difference constractor and factory : 
// factory use camel case
// constractor not returning object, but using this
// both creating object


// Getter and setter

const people = {
    fName: 'mita',
    lName: 'astuti',
    get fullNames() {
        return `${person.fName} ${person.lName}`
    },
    set fullNames(value) {
        const parts = value.split(' ')
        this.fName = parts[0]
        this.lName = parts[1]
    }
}

people.fullNames = 'John Smith'
console.log(people)