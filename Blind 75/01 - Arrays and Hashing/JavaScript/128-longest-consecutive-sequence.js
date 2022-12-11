const { performance } = require('perf_hooks');

class Solution {
  method(nums) {
    const nums_set = new Set(nums);

    let res = 0;
    for (const n of nums_set) {
      // Check start of sequence
      if (!nums_set.has(n - 1)) {
        let len = 1;
        while (nums_set.has(n + len)) {
          len += 1;
        }
        res = Math.max(res, len);
      }
    }

    return res;
  }

  reference(nums) {
    let len = nums.length;
    if (!len) {
      return 0;
    }
    const set = new Set(nums);
    let max = 0;

    for (let i = 0; i < nums.length; i++) {
      const num = nums[i];

      if (set.has(num - 1)) {
        continue;
      }

      let currentMax = 1;
      while (set.has(num + currentMax)) {
        currentMax++;
      }

      if (currentMax > max) {
        max = currentMax;
      }
      if (max > len / 2) {
        break;
      }
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
const testCases = [
  [100, 4, 200, 1, 3, 2],
  [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
];
test.quantify(testCases);
