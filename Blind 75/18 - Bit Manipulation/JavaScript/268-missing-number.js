const { performance } = require("perf_hooks");

class Solution {
  method(nums) {
    let res = nums.length;
    for (let i = 0; i < nums.length; i++) {
      res ^= i ^ nums[i];
    }

    return res;
  }

  reference(nums, missingNumber = nums.length) {
    for (let i = 0; i < nums.length; i++) {
      const xor = i ^ nums[i];

      missingNumber ^= xor;
    }

    return missingNumber;
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
  [3, 0, 1],
  [0, 1],
  [9, 6, 4, 2, 3, 5, 7, 0, 1],
];
test.quantify(testCases);
