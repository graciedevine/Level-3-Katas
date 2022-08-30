// Given an array of integers your solution should find the smallest integer.

// For example:

//     Given [34, 15, 88, 2] your solution will return 2


function SmallestIntegerFinder(arr) {
  console.log(Math.min.apply(null, arr))
}

SmallestIntegerFinder([34, 15, 88, 2])