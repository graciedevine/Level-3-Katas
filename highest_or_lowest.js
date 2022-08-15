// In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

// Add commas in between numbers?
// Remove whitespaces?
// Convert str to int
// return max and min values

function highAndLow(numbers) {
    // .split() splits a string into an array of substrings, and returns the array
    numbers = numbers.split(" ");
    // .apply() write a method, arguements provided are arrays
    return Math.max.apply(null, numbers) + " " + Math.min.apply(null, numbers)
}

highAndLow("1 2 3 4 5");