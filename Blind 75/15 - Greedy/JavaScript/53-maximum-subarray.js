const { performance } = require("perf_hooks");

class Solution {
  method(nums) {
    let [bestSum, total] = [0, 0];
    for (const n of nums) {
      total += n;
      bestSum = Math.max(bestSum, total);
      if (total < 0) total = 0;
    }

    return bestSum;
  }

  reference(nums) {
    let [runningSum, maxSum] = [nums[0], nums[0]];

    for (let i = 1; i < nums.length; i++) {
      const num = nums[i];
      const sum = runningSum + num;

      runningSum = Math.max(num, sum);
      maxSum = Math.max(maxSum, runningSum);
    }

    return maxSum;
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
const testCases = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8]];
test.quantify(testCases);
