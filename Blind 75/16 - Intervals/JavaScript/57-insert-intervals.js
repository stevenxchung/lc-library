const { performance } = require('perf_hooks');

class Solution {
  method(intervals, newInterval) {
    let res = [];
    for (let i = 0; i < intervals.length; i++) {
      if (newInterval[1] < intervals[i][0]) {
        res.push(newInterval);
        res.push(intervals.slice(i));
        return res;
      } else if (newInterval[0] > intervals[i][1]) {
        res.push(intervals[i]);
      } else {
        newInterval = [
          Math.min(newInterval[0], intervals[i][0]),
          Math.max(newInterval[1], intervals[i][1]),
        ];
      }
    }

    res.push(newInterval);
    return intervals;
  }

  reference(intervals, newInterval) {
    const { beforeIndex, before } = this.getBefore(intervals, newInterval);
    const afterIndex = this.mergeIntervals(intervals, newInterval, beforeIndex);
    const after = intervals.slice(afterIndex);

    return [...before, newInterval, ...after];
  }

  getBefore = (intervals, newInterval, index = 0, before = []) => {
    const hasGap = ([prevStart, prevEnd], [currStart, currEnd]) =>
      prevEnd < currStart;

    while (index < intervals.length && hasGap(intervals[index], newInterval)) {
      const current = intervals[index];

      before.push(current);
      index++;
    }

    return { beforeIndex: index, before };
  };

  mergeIntervals = (intervals, newInterval, index) => {
    const hasOverlap = ([prevStart, prevEnd], [currStart, currEnd]) =>
      currStart <= prevEnd;

    while (
      index < intervals.length &&
      hasOverlap(newInterval, intervals[index])
    ) {
      const current = intervals[index];

      newInterval[0] = Math.min(newInterval[0], current[0]);
      newInterval[1] = Math.max(newInterval[1], current[1]);
      index++;
    }

    return index;
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
  [
    [
      [1, 3],
      [6, 9],
    ],
    [2, 5],
  ],
  [
    [
      [1, 2],
      [3, 5],
      [6, 7],
      [8, 10],
      [12, 16],
    ],
    [4, 8],
  ],
];
test.quantify(testCases);
