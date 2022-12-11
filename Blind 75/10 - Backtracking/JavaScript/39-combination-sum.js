const { performance } = require('perf_hooks');

class Solution {
  method(candidates, target) {
    let res = [];
    candidates.sort();

    const dfs = (i, numbers, total) => {
      if (i >= candidates.length || total > target) return;
      if (total === target) {
        res.push([...numbers]);
        return;
      }

      numbers.push(candidates[i]);
      dfs(i, numbers, total + candidates[i]);
      numbers.pop();
      dfs(i + 1, numbers, total);
    };

    dfs(0, [], 0);
    return res;
  }

  reference(
    candidates,
    target,
    index = 0,
    combination = [],
    combinations = []
  ) {
    const isBaseCase = target < 0;
    if (isBaseCase) return combinations;

    const isTarget = target === 0;
    if (isTarget) return combinations.push(combination.slice());

    for (let i = index; i < candidates.length; i++) {
      this.backTrack(candidates, target, i, combination, combinations);
    }

    return combinations;
  }

  backTrack = (candidates, target, i, combination, combinations) => {
    combination.push(candidates[i]);
    this.reference(
      candidates,
      target - candidates[i],
      i,
      combination,
      combinations
    );
    combination.pop();
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(...input));
        else this.method(...input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
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
  [[2, 3, 6, 7], 7],
  [[2, 3, 5], 8],
  [[2], 1],
];
test.quantify(testCases);
