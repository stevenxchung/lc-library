/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
*/

let string = '()[]{}';

let isValid = s => {
  // Initialize hash table of bracket types
  let bracketType = { ')': '(', '}': '{', ']': '[' };
  // Use stack
  let stack = [];
  // Top of stack
  let top = '';
  // Spread string
  s = [...s];

  for (let i = 0; i < s.length; i++) {
    // Check if s[i] is in hash map
    if (bracketType[s[i]]) {
      // Top is either the top of the stack or ''
      top = stack.length !== 0 ? stack.pop() : '';
      // Bracket does not match
      if (bracketType[s[i]] !== top) {
        return false;
      }
    } else {
      stack.push(s[i]);
    }
  }

  // If stack is not empty then return false
  if (stack.length !== 0) {
    return false
  }

  return true;
};

console.log(isValid(string));
