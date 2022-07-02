/*
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
*/

/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function (n) {
    arr = []
    while (n > 0) {
        if (n % 15 === 0) {
            arr.unshift('FizzBuzz');
        } else if (n % 3 === 0) {
            arr.unshift('Fizz');
        } else if (n % 5 === 0) {
            arr.unshift('Buzz');
        } else {
            arr.unshift(`${n}`);
        }
        n -= 1;
    }
    return arr;
};

console.log(fizzBuzz(3))