const { performance } = require('perf_hooks');

class Solution {
  method(nums, k) {
    let counts = {};
    let bucket = Array.from({ length: nums.length + 1 }, () => []);
    for (const n of nums) {
      if (n in counts) {
        counts[n] += 1;
      } else {
        counts[n] = 1;
      }
    }
    for (const [v, count] of Object.entries(counts)) {
      bucket[count].push(v);
    }
    const mostFrequent = bucket
      .filter((e) => e.length > 0)
      .slice(-k)
      .reduce((a, b) => a.concat(b)); // Can also use flat()

    return mostFrequent;
  }

  reference(nums, k) {
    let map = {};
    let res = [];
    let bucket = Array.from({ length: nums.length + 1 }, () => []); // To create unique arrays

    // Storing frequency of numbers in a map
    for (const n of nums) {
      map[n] = n in map ? 1 + map[n] : 1;
    }

    // Populate the bucket with numbers in frequency
    // as the index of the bucket
    for (const c in map) {
      bucket[map[c]].push(c);
    }

    for (let i = bucket.length - 1; i >= 0; i--) {
      if (bucket[i].length > 0) {
        bucket[i].forEach((elem) => res.push(elem));
        if (k == res.length) {
          return res;
        }
      }
    }
  }

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
  [[1, 1, 1, 2, 2, 3], 2],
  [[1], 1],
];
test.quantify(testCases);
