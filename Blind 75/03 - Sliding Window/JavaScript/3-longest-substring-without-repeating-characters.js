const { performance } = require('perf_hooks');

class Solution {
  method(s) {
    const seen = new Set();

    let l = 0;
    let res = 0;
    for (let r = 0; r < s.length; r++) {
      // Remove earliest character if seen
      while (seen.has(s[r])) {
        seen.delete(s[l]);
        l += 1;
      }
      seen.add(s[r]);
      res = Math.max(res, seen.size);
    }

    return res;
  }

  reference(s) {
    const set = new Set();
    let l = 0;
    let max = 0;

    for (let r = 0, sl = s.length; r < sl; r++) {
      while (set.has(s[r])) {
        set.delete(s[l]);
        l++;
      }

      set.add(s[r]);
      max = Math.max(max, set.size);
    }
    return max;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(input));
        else this.method(input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
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
const testCases = ['abcabcbb', 'bbbbb', 'pwwkew'];
test.quantify(testCases);
