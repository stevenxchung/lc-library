const { performance } = require('perf_hooks');

class Solution {
  method(intervals) {
    let count = 0;
    let prevEnd = -Infinity;
    intervals.sort((a, b) => a[0] - b[0]);
    for (const [start, end] of intervals) {
      if (prevEnd && prevEnd > start) {
        count += 1;
        prevEnd = Math.min(prevEnd, end);
      } else {
        prevEnd = end;
      }
    }

    return count;
  }

  reference(intervals) {
    intervals.sort(([aStart, aEnd], [bStart, bEnd]) =>
      aEnd !== bEnd ? aEnd - bEnd : aStart - bStart
    );

    return this.getGaps(intervals);
  }

  getGaps = (intervals, gaps = 1) => {
    const prev = intervals.shift();

    for (const curr of intervals) {
      const [prevStart, prevEnd] = prev;
      const [currStart, currEnd] = curr;

      const hasGap = prevEnd <= currStart;
      if (!hasGap) continue;

      prev[1] = curr[1];
      gaps++;
    }

    return intervals.length + 1 - gaps;
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
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
  ],
  [
    [1, 2],
    [1, 2],
    [1, 2],
  ],
  [
    [1, 2],
    [2, 3],
  ],
];
test.quantify(testCases);
