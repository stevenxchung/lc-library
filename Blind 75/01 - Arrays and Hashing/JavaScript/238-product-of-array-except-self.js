const { performance } = require("perf_hooks");

class Solution {
  method(nums) {
    let [prefix, suffix] = [1, 1];
    let res = [];
    for (const [i, n] of nums.entries()) {
      res[i] = prefix;
      prefix *= n;
    }

    for (let i = nums.length - 1; i >= 0; i--) {
      res[i] *= suffix;
      suffix *= nums[i];
    }

    return res;
  }

  reference(nums) {
    const result = [];
    let prefix = 1;
    let postfix = 1;

    for (let i = 0; i < nums.length; i++) {
      result[i] = prefix;
      prefix *= nums[i];
    }
    for (let i = nums.length - 2; i >= 0; i--) {
      postfix *= nums[i + 1];
      result[i] *= postfix;
    }

    return result;
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
const testCases = [
  [1, 2, 3, 4],
  [-1, 1, 0, -3, 3],
];
test.quantify(testCases);
