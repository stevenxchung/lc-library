const { performance } = require('perf_hooks');

class Solution {
  method(nums) {
    let [prev, curr] = [0, 0];
    for (const n of nums) {
      [prev, curr] = [curr, Math.max(curr, prev + n)];
    }

    return curr;
  }

  reference(nums, i = 0, memo = this.initMemo(nums)) {
    const isBaseCase = nums.length <= i;
    if (isBaseCase) return 0;

    const hasSeen = 0 <= memo[i];
    if (hasSeen) return memo[i];

    const [next, nextNext] = [i + 1, i + 2];
    const right = nums[i];
    const mid = this.reference(nums, next, memo); /* Time O(N) | Space O(N) */
    const left = this.reference(
      nums,
      nextNext,
      memo
    ); /* Time O(N) | Space O(N) */
    const house = left + right;

    memo[i] = Math.max(mid, house); /*           | Space O(N) */

    return memo[i];
  }

  initMemo = (nums) => Array(nums.length + 1).fill(-1);

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
  [1, 2, 3, 1],
  [2, 7, 9, 3, 1],
];
test.quantify(testCases);
