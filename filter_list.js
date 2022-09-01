// In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

// Example: filter_list([1,2,'a','b']) == [1,2]

// typeof(val)
// interator method to extract numbers .filter() or .map()



function filter_list(l) {
    return filtered = l.filter(elem => typeof (elem) === 'number');
    // return l.filter(Number.isInteger);
}

filter_list([1, 2, 'a', 'b', 'c'])

