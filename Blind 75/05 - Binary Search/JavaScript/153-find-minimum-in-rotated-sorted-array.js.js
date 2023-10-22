const { performance } = require("perf_hooks");

class Solution {
  method(nums) {
    let [l, r] = [0, nums.length - 1];
    while (l < r) {
      const m = Math.floor((l + r) / 2);
      // Right portion not sorted
      if (nums[m] > nums[r]) l = m + 1;
      else r = m;
    }

    return nums[l];
  }

  reference(nums) {
    let [left, right] = [0, nums.length - 1];

    while (left < right) {
      const mid = (left + right) >> 1;
      const guess = nums[mid];
      const [leftNum, rightNum] = [nums[left], nums[right]];

      const isTarget = leftNum < rightNum;
      if (isTarget) return leftNum;

      const isTargetGreater = leftNum <= guess;
      if (isTargetGreater) left = mid + 1;

      const isTargetLess = guess < leftNum;
      if (isTargetLess) right = mid;
    }

    return nums[left];
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
  [3, 4, 5, 1, 2],
  [4, 5, 6, 7, 0, 1, 2],
  [11, 13, 15, 17],
];
test.quantify(testCases);
