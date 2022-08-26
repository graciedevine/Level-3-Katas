// Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

//     S is misinterpreted as 5
//     O is misinterpreted as 0
//     I is misinterpreted as 1

function correct(string) {
    console.log(string.replace(/5/g, "S").replace(/0/g, "O").replace(/1/g, "I"))
}

correct("L0ND0N")