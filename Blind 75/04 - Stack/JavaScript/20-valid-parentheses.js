const { performance } = require("perf_hooks");

class Solution {
  method(s) {
    const table = {
      ")": "(",
      "}": "{",
      "]": "[",
    };

    let stack = [];

    for (const c of s) {
      if (!(c in table)) {
        stack.push(c);
        continue;
      }
      if (stack.length === 0 || stack.slice(-1)[0] !== table[c]) return false;
      stack.pop();
    }

    return true;
  }

  reference(s) {
    if (!s) return false;
    let closeMap = {
      "}": "{",
      "]": "[",
      ")": "(",
    };
    let stack = [];
    for (const str of s) {
      if (str in closeMap) {
        if (stack.length !== 0 && stack.slice(-1)[0] === closeMap[str]) {
          stack.pop();
        } else {
          return false;
        }
      } else {
        stack.push(str);
      }
    }
    return stack.length === 0;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(input));
        else this.method(input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(input));
        else this.reference(input);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}

const test = new Solution();
const testCases = ["()", "()[]{}", "(]"];
test.quantify(testCases);
