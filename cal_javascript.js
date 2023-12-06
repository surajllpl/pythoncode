const prompt = require("prompt-sync")({sigint:true});
console.log("Hello Word")


let f_no = parseInt(prompt("Enter first no"));
op = prompt("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n");
s_no = parseInt(prompt("Enter second no :- "));

console.log(f_no + s_no)