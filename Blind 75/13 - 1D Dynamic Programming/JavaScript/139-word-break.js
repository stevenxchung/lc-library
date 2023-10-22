const { performance } = require("perf_hooks");

class Solution {
  method(s, wordDict) {
    let queue = [s];
    let found = new Set();

    while (queue.length > 0) {
      const s = queue.shift();
      for (const w of wordDict) {
        if (s.startsWith(w)) {
          const newS = s.slice(w.length, s.length);
          if (newS === "") return true;
          if (!(newS in found)) {
            queue.push(newS);
            found.add(newS);
          }
        }
      }
    }

    return false;
  }

  reference(s, wordDict) {
    const wordSet = new Set(wordDict); /* Time O(N) | Space O(N) */
    const memo = new Array(s.length).fill(null); /* | Space O(N) */
    const start = 0;

    return this.canBreak(
      s,
      wordSet,
      start,
      memo
    ); /* Time O(N * N * N) | Space O(N) */
  }

  canBreak = (s, wordSet, start, memo) => {
    const isBaseCase1 = s.length === start;
    if (isBaseCase1) return true;

    const hasSeen = memo[start] !== null;
    if (hasSeen) return memo[start];

    return this.dfs(
      s,
      wordSet,
      start,
      memo
    ); /* Time O(N * N * N) | Space O(N) */
  };

  dfs = (s, wordSet, start, memo) => {
    for (let end = start + 1; end <= s.length; end++) {
      /* Time O(N) */
      const word = s.slice(start, end); /* Time O(N) | Space O(N) */

      const _canBreak =
        wordSet.has(word) &&
        this.canBreak(s, wordSet, end, memo); /* Time O(N * N) */
      if (_canBreak) {
        memo[start] = true;
        return true;
      }
    }

    memo[start] = false;
    return false;
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
  ["leetcode", ["leet", "code"]],
  ["applepenapple", ["apple", "pen"]],
  ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
  // Additional
  ["bb", ["a", "b", "bbb", "bbbb"]],
  ["aaaaaaa", ["aaaa", "aaa"]],
  ["aaaaaa", ["aa", "a"]],
];
test.quantify(testCases);
