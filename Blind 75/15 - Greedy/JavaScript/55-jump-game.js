const { performance } = require("perf_hooks");

class Solution {
  method(nums) {
    let target = nums.length - 1;
    for (let i = nums.length - 2; i >= 0; i--) {
      if (i + nums[i] >= target) target = i;
    }

    return target === 0;
  }

  reference(nums, right = nums.length - 1) {
    for (let i = right; 0 <= i; i--) {
      const isJumpable = right <= i + nums[i];
      if (isJumpable) right = i;
    }

    return right === 0;
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
  [2, 3, 1, 1, 4],
  [3, 2, 1, 0, 4],
  // Additional
  [0, 2, 3],
];
test.quantify(testCases);
