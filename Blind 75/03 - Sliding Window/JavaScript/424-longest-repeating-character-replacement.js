const { performance } = require("perf_hooks");

class Solution {
  method(s, k) {
    let count = {};
    let res = 0;

    let l = 0;
    let maxFrequency = 0;
    for (let r = 0; r < s.length; r++) {
      count[s[r]] = s[r] in count ? 1 + count[s[r]] : 1;
      maxFrequency = Math.max(maxFrequency, count[s[r]]);

      // Where r - l + 1 is the window length
      if (r - l + 1 - maxFrequency > k) {
        count[s[l]] -= 1;
        l += 1;
      }

      res = Math.max(res, r - l + 1);
    }

    return res;
  }

  reference(s, k) {
    let [left, right, longest, max] = new Array(4).fill(0);
    const frequencyMap = new Array(26).fill(0);

    while (right < s.length) {
      const count = this.addRightFrequency(s, right, frequencyMap);

      longest = Math.max(longest, count);

      let window = right - left + 1;
      const canSlide = k < window - longest;
      if (canSlide) {
        this.subtractLeftFrequency(s, left, frequencyMap);
        left++;
      }

      window = right - left + 1;
      max = Math.max(max, window);

      right++;
    }

    return max;
  }

  addRightFrequency = (s, right, map) => {
    const char = s[right];
    const index = this.getCode(char);

    map[index]++;

    return map[index];
  };

  subtractLeftFrequency = (s, left, map) => {
    const char = s[left];
    const index = this.getCode(char);

    map[index]--;

    return map[index];
  };

  getCode = (char) => char.charCodeAt(0) - "A".charCodeAt(0);

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
  ["ABAB", 2],
  ["AABABBA", 1],
];
test.quantify(testCases);
