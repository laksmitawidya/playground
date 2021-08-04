const numbers = [1, -1, 2, 3]
const filtered = numbers.filter(n => n >= 0)
console.log(filtered)


// accumulator : intial will be the first element, current value will walk through the index of the array
// a = 0, c = 1 => a = 1
// a = 1, c = -1 => a = 0
// a = 0, c = 2 => a = 2
// a = 2, c = 3 => a = 5

// that code same with this
// let sum = 0
// for (let n of numbers){
//     sum +=n
// }

// a = 1, c = -1 => a = 0
// a =0, c = 2 => a = 2
// a = 2, c = 3 => a = 5

// with the return statement
const sum = numbers.reduce((accumulator, currentValue) => {
    return accumulator + currentValue
}, 0)

// without return statement
const sum2 = numbers.reduce((accumulator, currentValue) => accumulator + currentValue)
console.log(sum)

// array map
const items = filtered.map(n => ({ value: n }))


// chaining multiple method, method return some method and return again some another method
numbers
    .filter(n => n >= 0)
    .map(n => ({ value: n }))
    .filter(obj => obj.value >= 1)
    .map(obj => { obj.value })


console.log(items)