const { performance } = require('perf_hooks');

class Solution {
  method(nums) {
    let res = [];
    let seen = new Set();
    const sortedNums = nums.sort((a, b) => a - b);
    for (const [i, a] of sortedNums.entries()) {
      // Skip duplicates
      if (seen.has(a)) continue;

      let [j, k] = [i + 1, nums.length - 1];
      while (j < k) {
        const total = a + nums[j] + nums[k];
        if (total > 0) k -= 1;
        else if (total < 0) j += 1;
        else {
          res.push([a, nums[j], nums[k]]);
          j += 1;
          // Skip duplicates
          while (seen.has(nums[j]) && j < k) {
            j += 1;
          }
        }
      }
      seen.add(a);
    }

    return res;
  }

  reference(nums, sums = []) {
    nums.sort((a, b) => a - b);

    for (let first = 0; first < nums.length - 2; first++) {
      if (this.isPrevDuplicate(nums, first)) continue;

      const [target, left, right] = [-nums[first], first + 1, nums.length - 1];

      this.search(nums, target, left, right, sums);
    }

    return sums;
  }

  isPrevDuplicate = (nums, index) => nums[index - 1] === nums[index];

  isNextDuplicate = (nums, index) => nums[index] === nums[index + 1];

  search = (nums, target, left, right, sums) => {
    while (left < right) {
      const [leftVal, rightVal] = [nums[left], nums[right]];
      const sum = leftVal + rightVal;

      const isTarget = sum === target;
      if (isTarget) {
        sums.push([-target, leftVal, rightVal]);
        left++;
        right--;

        while (left < right && this.isPrevDuplicate(nums, left)) left++;
        while (left < right && this.isNextDuplicate(nums, right)) right--;

        continue;
      }

      const isTargetGreater = sum < target;
      if (isTargetGreater) left++;

      const isTargetLess = target < sum;
      if (isTargetLess) right--;
    }
  };

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
const testCases = [
  [-1, 0, 1, 2, -1, -4],
  [0, 1, 1],
  [0, 0, 0],
];
test.quantify(testCases);
