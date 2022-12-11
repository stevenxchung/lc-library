const { performance } = require('perf_hooks');

class Solution {
  method(prices) {
    let profit = 0;

    let l = 0;
    for (let r = 1; r < prices.length; r++) {
      // Set left to right if right is less (no profit)
      if (prices[r] < prices[l]) l = r;
      profit = Math.max(profit, prices[r] - prices[l]);
    }

    return profit;
  }

  reference(prices) {
    let [left, right, max] = [0, 1, 0];

    while (right < prices.length) {
      const canSlide = prices[right] <= prices[left];
      if (canSlide) left = right;

      const window = prices[right] - prices[left];

      max = Math.max(max, window);
      right++;
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
  [7, 1, 5, 3, 6, 4],
  [7, 6, 4, 3, 1],
];
test.quantify(testCases);
