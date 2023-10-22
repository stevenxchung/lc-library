const { performance } = require("perf_hooks");

class Solution {
  method(n, edges) {
    let adjList = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
      adjList[a].push(b);
    }

    let seen = new Set();

    const dfs = (curr, prev) => {
      if (seen.has(curr)) return false;

      seen.add(curr);
      for (const n of adjList[curr]) {
        if (n === prev) continue;
        if (!dfs(n, curr)) return false;
      }

      return true;
    };

    return dfs(0, -1) && seen.size === n;
  }

  reference(n, edges) {
    const union = new Array(n).fill(-1);

    for (const [src, dst] of edges) {
      const [x, y] = [this.find(union, src), this.find(union, dst)];

      const hasCycle = x === y;
      if (hasCycle) return false;

      this.compress(union, x, y);
    }

    const isValid = edges.length === n - 1;
    return isValid;
  }

  compress = (union, i, head) => (union[i] = head);

  find = (union, i, num = union[i]) => {
    const isEmpty = num === -1;
    if (isEmpty) return i;

    const head = this.find(union, num);

    this.compress(union, i, head);

    return union[i];
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
  [
    5,
    [
      [0, 1],
      [0, 2],
      [0, 3],
      [1, 4],
    ],
  ],
  // Additional
  [
    7,
    [
      [0, 1],
      [0, 2],
      [3, 5],
      [5, 6],
      [1, 4],
    ],
  ],
];
test.quantify(testCases);
