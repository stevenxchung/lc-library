const { performance } = require('perf_hooks');

class Solution {
  method(n) {
    let res = Array.from({ length: n + 1 }, () => 0);
    let offset = 1;
    for (let i = 1; i < n + 1; i++) {
      if (offset * 2 === i) {
        offset = i;
      }
      res[i] = 1 + res[i - offset];
    }

    return res;
  }

  reference(n, dp = [0]) {
    for (let i = 1; i < n + 1; i++) {
      const [mid, bit] = [i >> 1, i & 1];
      const bits = dp[mid] + bit;

      dp.push(bits);
    }

    return dp;
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
const testCases = [2, 5];
test.quantify(testCases);
