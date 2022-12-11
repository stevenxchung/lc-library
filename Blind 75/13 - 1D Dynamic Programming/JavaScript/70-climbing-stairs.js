const { performance } = require('perf_hooks');

class Solution {
  method(n) {
    const steps = { 1: 1, 2: 2 };
    const dfs = (n) => {
      if (!(n in steps)) steps[n] = dfs(n - 1) + dfs(n - 2);
      return steps[n];
    };

    return dfs(n);
  }

  reference(n, index = 0) {
    const isBaseCase1 = n < index;
    if (isBaseCase1) return 0;

    const isBaseCase2 = index === n;
    if (isBaseCase2) return 1;

    const [next, nextNext] = [index + 1, index + 2];
    const left = this.reference(n, next); /* Time O(2^N) | Space O(N) */
    const right = this.reference(n, nextNext); /* Time O(2^N) | Space O(N) */

    return left + right;
  }

  dfs = (char, graph, seen, buffer) => {
    if (seen.has(char)) return seen.get(char);

    if (!this.backTrack(char, graph, seen, buffer)) return false;

    buffer.push(char);

    return true;
  };

  backTrack = (char, graph, seen, buffer) => {
    seen.set(char, false);
    for (const neighbor of graph.get(char)) {
      if (!this.dfs(neighbor, graph, seen, buffer)) return false;
    }
    seen.set(char, true);

    return true;
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
const testCases = [2, 3];
test.quantify(testCases);
