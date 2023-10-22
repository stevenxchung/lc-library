const { performance } = require("perf_hooks");

class Solution {
  method(nums, target) {
    let numToIndexMap = {};
    for (const [i, n] of nums.entries()) {
      const diff = target - n;
      if (diff in numToIndexMap) return [numToIndexMap[diff], i];
      numToIndexMap[n] = i;
    }
  }

  reference(nums, target) {
    let map = {};
    for (let i = 0; i < nums.length; i++) {
      if (target - nums[i] in map) {
        return [map[target - nums[i]], i];
      } else {
        map[nums[i]] = i;
      }
    }
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
  [[2, 7, 11, 15], 9],
  [[3, 2, 4], 6],
  [[3, 3], 6],
];
test.quantify(testCases);
