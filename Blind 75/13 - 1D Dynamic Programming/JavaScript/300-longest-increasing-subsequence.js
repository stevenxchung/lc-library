const { performance } = require('perf_hooks');

class Solution {
  method(nums) {
    let cache = Array.from({ length: nums.length }, () => 1);

    for (let i = nums.length - 1; i >= 0; i--) {
      for (let j = i + 1; j < nums.length; j++) {
        if (nums[i] < nums[j]) cache[i] = Math.max(cache[i], 1 + cache[j]);
      }
    }

    return Math.max(...cache);
  }

  reference(nums) {
    const subsequence = this.logarithmicSort(nums); /* Time O(N * log(N) */

    return subsequence.length;
  }

  logarithmicSort = (nums, subsequence = []) => {
    for (const num of nums) {
      /* Time O(N) */
      const max = subsequence[subsequence.length - 1];

      const canAdd = max < num;
      if (canAdd) {
        subsequence.push(num);
        continue;
      } /* Space O(N) */

      const index = this.binarySearch(num, subsequence); /* Time O(log(N)) */

      subsequence[index] = num;
    }

    return subsequence;
  };

  binarySearch = (num, subsequence) => {
    let [left, right] = [0, subsequence.length - 1];

    while (left < right) {
      /* Time O(log(N)) */
      const mid = (left + right) >> 1;
      const guess = subsequence[mid];

      const isNumTarget = num === guess;
      if (isNumTarget) return mid;

      const isNumGreater = guess < num;
      if (isNumGreater) left = mid + 1;

      const isNumLess = num < guess;
      if (isNumLess) right = mid;
    }

    return left;
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
  [10, 9, 2, 5, 3, 7, 101, 18],
  [0, 1, 0, 3, 2, 3],
  [7, 7, 7, 7, 7, 7, 7],
];
test.quantify(testCases);
