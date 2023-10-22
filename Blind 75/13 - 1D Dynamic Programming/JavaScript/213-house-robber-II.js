const { performance } = require("perf_hooks");

class Solution {
  method(nums) {
    const robHelper = (nums) => {
      let [prev, curr] = [0, 0];
      for (const n of nums) {
        [prev, curr] = [curr, Math.max(curr, prev + n)];
      }
      return curr;
    };

    return Math.max(
      nums[0],
      robHelper(nums.slice(1)),
      robHelper(nums.slice(0, -1))
    );
  }

  reference(nums) {
    const isBaseCase1 = nums.length === 0;
    if (isBaseCase1) return 0;

    const isBaseCase2 = nums.length === 1;
    if (isBaseCase2) return nums[0];

    const left = this.search(nums, 0, nums.length - 2); /* Time O(N) */
    const right = this.search(nums, 1, nums.length - 1); /* Time O(N) */

    return Math.max(left, right);
  }

  search = (nums, start, end) => {
    let [left, mid] = [0, 0];

    for (let i = start; i <= end; i++) {
      /* Time O(N) */
      const temp = mid;
      const right = nums[i];
      const house = left + right;

      mid = Math.max(mid, house);
      left = temp;
    }

    return mid;
  };

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
  [2, 3, 2],
  [1, 2, 3, 1],
  [1, 2, 3],
];
test.quantify(testCases);
