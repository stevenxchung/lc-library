const { performance } = require('perf_hooks');

class Solution {
  method(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    for (let i = 1; i < intervals.length; i++) {
      if (intervals[i - 1][1] > intervals[i][0]) return false;
    }

    return true;
  }

  reference(intervals) {
    intervals.sort(([aStart, aEnd], [bStart, bEnd]) =>
      aStart !== bStart ? aStart - bStart : aEnd - bEnd
    );

    return this.canAttend(intervals);
  }

  canAttend = (intervals) => {
    let prev = intervals.shift();

    for (const curr of intervals) {
      const [prevStart, prevEnd] = prev;
      const [currStart, currEnd] = curr;

      const hasOverlap = currStart < prevEnd;
      if (hasOverlap) return false;

      prev = curr;
    }

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
const testCases = [
  [
    [0, 30],
    [5, 10],
    [15, 20],
  ],
  // Additional
  [
    [5, 10],
    [15, 20],
    [0, 30],
  ],
];
test.quantify(testCases);
