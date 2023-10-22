const { performance } = require("perf_hooks");

class Solution {
  method(coins, amount) {
    let cache = Array.from({ length: amount + 1 }, () => amount + 1);
    cache[0] = 0;

    for (let n = 1; n < amount + 1; n++) {
      for (const c of coins) {
        if (n - c >= 0) cache[n] = Math.min(cache[n], 1 + cache[n - c]);
      }
    }

    return cache[amount] !== amount + 1 ? cache[amount] : -1;
  }

  reference(coins, amount, memo = this.initMemo(amount)) {
    const isBaseCase1 = amount < 0;
    if (isBaseCase1) return -1;

    const isBaseCase2 = amount < 1;
    if (isBaseCase2) return 0;

    const isBaseCase3 = memo[amount - 1] !== 0;
    if (isBaseCase3) return memo[amount - 1];

    return this.dfs(coins, amount, memo); /* Time O(N) | Space O(N) */
  }

  initMemo = (amount) => Array(amount).fill(0);

  dfs = (coins, amount, memo, min = Infinity) => {
    for (const coin of coins) {
      /* Time O(N) */
      const cost = this.reference(
        coins,
        amount - coin,
        memo
      ); /* Time O(N) | Space O(N) */

      const canUpdate = 0 <= cost && cost < min;
      if (!canUpdate) continue;

      min = cost + 1;
    }

    memo[amount - 1] = min !== Infinity ? min : -1;

    return memo[amount - 1];
  };

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
  [[1, 2, 5], 11],
  [[2], 3],
  [[1], 0],
];
test.quantify(testCases);
