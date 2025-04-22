const { performance } = require("perf_hooks");

class Solution {
  method(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    let res = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
      const lastInterval = res[res.length - 1];
      if (lastInterval[1] >= intervals[i][0]) {
        lastInterval[1] = Math.max(lastInterval[1], intervals[i][1]);
      } else {
        res.push(intervals[i]);
      }
    }

    return res;
  }

  reference(intervals) {
    intervals.sort(([aStart, aEnd], [bStart, bEnd]) =>
      aStart !== bStart ? aStart - bStart : aEnd - bEnd
    );

    return this.mergerInterval(intervals);
  }

  mergerInterval = (intervals, merged = []) => {
    let prev = intervals.shift();

    for (const curr of intervals) {
      const [prevStart, prevEnd] = prev;
      const [currStart, currEnd] = curr;

      const hasOverlap = currStart <= prevEnd;
      if (hasOverlap) {
        prev[1] = Math.max(prev[1], curr[1]);
        continue;
      }

      merged.push(prev);
      prev = curr;
    }

    return [...merged, prev];
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
  [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18],
  ],
  [
    [1, 4],
    [4, 5],
  ],
  // Additional
  [
    [1, 4],
    [0, 4],
  ],
];
test.quantify(testCases);
