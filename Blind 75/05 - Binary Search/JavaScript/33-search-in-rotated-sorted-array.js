const { performance } = require("perf_hooks");

class Solution {
  method(nums, target) {
    let [l, r] = [0, nums.length - 1];
    while (l <= r) {
      const m = l + Math.floor((r - l) / 2);
      if (target === nums[m]) return m;

      if (nums[l] <= nums[m]) {
        // Left portion properly sorted
        if (target > nums[m] || target < nums[l]) l = m + 1;
        else r = m - 1;
      } else {
        // Right portion properly sorted
        if (target < nums[m] || target > nums[r]) r = m - 1;
        else l = m + 1;
      }
    }
    return -1;
  }

  reference(nums, target) {
    let [left, right] = [0, nums.length - 1];

    while (left <= right) {
      const mid = (left + right) >> 1;
      const guess = nums[mid];
      const [leftNum, rightNum] = [nums[left], nums[right]];

      const isTarget = guess === target;
      if (isTarget) return mid;

      const isAscending = leftNum <= guess;
      if (isAscending) {
        const isInRange = leftNum <= target;
        const isLess = target < guess;

        const isTargetGreater = !(isInRange && isLess);
        if (isTargetGreater) left = mid + 1;

        const isTargetLess = isInRange && isLess;
        if (isTargetLess) right = mid - 1;
      }

      const isDescending = guess < leftNum;
      if (isDescending) {
        const isGreater = guess < target;
        const isInRange = target <= rightNum;

        const isTargetGreater = isGreater && isInRange;
        if (isTargetGreater) left = mid + 1;

        const isTargetLess = !(isGreater && isInRange);
        if (isTargetLess) right = mid - 1;
      }
    }

    return -1;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(...input));
        else this.method(...input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(...input));
        else this.reference(...input);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}

const test = new Solution();
const testCases = [
  [[4, 5, 6, 7, 0, 1, 2], 0],
  [[4, 5, 6, 7, 0, 1, 2], 3],
  [[1], 0],
];
test.quantify(testCases);
