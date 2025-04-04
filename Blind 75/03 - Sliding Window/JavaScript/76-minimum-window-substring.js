const { performance } = require("perf_hooks");

class Solution {
  method(s, t) {
    if (s.length < t.length) return "";

    // To store frequency of characters in t
    const charCount = new Array(128).fill(0);
    for (const c of t) {
      charCount[c.charCodeAt(0)]++;
    }

    let required = t.length;
    let l = 0;
    let [minL, minLength] = [0, Infinity];

    for (let r = 0; r < s.length; r++) {
      // Expand the window by including s[r]
      const indexR = s[r].charCodeAt(0);

      // Decrease the required count if the character is in t
      if (charCount[indexR] > 0) required--;
      charCount[indexR]--;

      // Once all characters are in the window, try to shrink it
      while (required === 0) {
        const indexL = s[l].charCodeAt(0);

        // Update the minimum window if this is smaller
        if (r - l + 1 < minLength) {
          minLength = r - l + 1;
          minL = l;
        }

        // Shrink the window by moving left pointer
        charCount[indexL]++;
        if (charCount[indexL] > 0) required++;
        l++;
      }
    }

    return minLength === Infinity ? "" : s.substring(minL, minL + minLength);
  }

  reference(s, t) {
    const isMissingArgs = !s.length || !t.length;
    if (isMissingArgs) return "";

    const frequencyMap = this.getFrequencyMap(t);
    const { start, end } = this.getWindowPointers(s, t, frequencyMap);

    return this.getSubString(s, start, end);
  }

  getFrequencyMap = (str, frequencyMap = new Map()) => {
    for (const char of str) {
      frequencyMap.set(char, (frequencyMap.get(char) || 0) + 1);
    }

    return frequencyMap;
  };

  getWindowPointers = (s, t, frequencyMap) => {
    let [left, right, matched, start, end] = [0, 0, 0, 0, s.length + 1];

    while (right < s.length) {
      matched = this.addRightFrequency(s, right, frequencyMap, matched);

      const canSlide = () => matched === t.length;
      while (canSlide()) {
        const window = right - left + 1;

        const isSmaller = window < end;
        if (isSmaller) {
          [start, end] = [left, window];
        }

        matched = this.subtractLeftFrequency(s, left, frequencyMap, matched);
        left++;
      }

      right++;
    }

    return { start, end };
  };

  addRightFrequency = (s, right, frequencyMap, matched) => {
    const char = s[right];

    if (frequencyMap.has(char)) {
      frequencyMap.set(char, frequencyMap.get(char) - 1);

      const isInWindow = 0 <= frequencyMap.get(char);
      if (isInWindow) matched++;
    }

    return matched;
  };

  subtractLeftFrequency = (s, left, frequencyMap, matched) => {
    const char = s[left];

    if (frequencyMap.has(char)) {
      const isOutOfWindow = frequencyMap.get(char) === 0;
      if (isOutOfWindow) matched--;

      frequencyMap.set(char, frequencyMap.get(char) + 1);
    }

    return matched;
  };

  getSubString = (s, start, end) =>
    end <= s.length ? s.slice(start, start + end) : "";

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
  ["ADOBECODEBANC", "ABC"],
  ["a", "a"],
  ["a", "aa"],
];
test.quantify(testCases);
