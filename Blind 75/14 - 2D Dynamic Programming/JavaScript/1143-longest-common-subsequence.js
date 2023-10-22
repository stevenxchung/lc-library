const { performance } = require("perf_hooks");

class Solution {
  method(text1, text2) {
    let cache2D = Array.from({ length: text1.length + 1 }, () =>
      Array.from({ length: text2.length + 1 }, () => 0)
    );

    for (let i = text1.length - 1; i >= 0; i--) {
      for (let j = text2.length - 1; j >= 0; j--) {
        if (text1[i] === text2[j]) {
          cache2D[i][j] = 1 + cache2D[i + 1][j + 1];
        } else if (text1[i] !== text2[j]) {
          cache2D[i][j] = Math.max(cache2D[i + 1][j], cache2D[i][j + 1]);
        }
      }
    }

    return cache2D[0][0];
  }

  reference(text1, text2, p1 = 0, p2 = 0, memo = this.initMemo(text1, text2)) {
    const isBaseCase = p1 === text1.length || p2 === text2.length;
    if (isBaseCase) return 0;

    const hasSeen = memo[p1][p2] !== null;
    if (hasSeen) return memo[p1][p2];

    return this.dfs(
      text1,
      text2,
      p1,
      p2,
      memo
    ); /* Time O(N * M) | Space O((N * M) + HEIGHT) */
  }

  initMemo = (text1, text2) =>
    new Array(text1.length + 1)
      .fill() /* Time O(N) | Space O(N) */
      .map(() =>
        new Array(text2.length + 1).fill(null)
      ); /* Time O(M) | Space O(M) */

  dfs = (text1, text2, p1, p2, memo) => {
    const left =
      this.reference(text1, text2, p1 + 1, p2 + 1, memo) +
      1; /* Time O(N * M) | Space O(HEIGHT) */
    const right =
      /* Time O(N * M) | Space O(HEIGHT) */
      Math.max(
        this.reference(text1, text2, p1, p2 + 1, memo),
        this.reference(text1, text2, p1 + 1, p2, memo)
      );

    const isEqual = text1[p1] == text2[p2];
    const count = isEqual ? left : right;

    memo[p1][p2] = count; /*               | Space O(N * M) */
    return memo[p1][p2];
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
  ["abcde", "ace"],
  ["abc", "abc"],
  ["abc", "def"],
];
test.quantify(testCases);
