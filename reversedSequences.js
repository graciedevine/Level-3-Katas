// Build a function that returns an array of integers from n to 1 where n>0.
// Example : n=5 --> [5,4,3,2,1]

//start with empty array
//start at 5, as long as n > 0, go down 1
//push 5 and each decresing value into array

const reverseSeq = n => {
    let arr = [];
    for (let i = n; i > 0; i--) {
        arr.push(i);
    }
    console.log(arr);
};

reverseSeq(5)