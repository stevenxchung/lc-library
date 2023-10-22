const { performance } = require("perf_hooks");

class Solution {
  method(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    let count = 1;
    for (let i = 1; i < intervals.length; i++) {
      if (intervals[i - 1][1] > intervals[i][0]) count += 1;
    }

    return count;
  }

  reference(intervals) {
    const { start, end } = this.splitIntervals(intervals);
    let [minRooms, startIndex, endIndex] = [0, 0, 0];

    while (startIndex < intervals.length) {
      const [currStart, prevEnd] = [start[startIndex], end[endIndex]];

      const hasGap = prevEnd <= currStart;
      if (hasGap) {
        minRooms--;
        endIndex++;
      }

      minRooms++;
      startIndex++;
    }

    return minRooms;
  }

  splitIntervals = (intervals, start = [], end = []) => {
    for (const [startTime, endTime] of intervals) {
      start.push(startTime);
      end.push(endTime);
    }

    const comparator = (a, b) => a - b;

    start.sort(comparator);
    end.sort(comparator);

    return { start, end };
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
