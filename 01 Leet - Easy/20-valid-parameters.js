/*

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

*/

let string = '[';

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
    if (bracketType[s[i]]) {
      top = stack ? stack.pop() : '';
      if (bracketType[s[i]] !== top) {
        return false;
      }
    } else {
      stack.push(s[i]);
    }
  }

  return !stack;
};

console.log(isValid(string));

/*
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
*/
