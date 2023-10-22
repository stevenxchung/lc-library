const { performance } = require("perf_hooks");

class Solution {
  method(s, t) {
    if (t.length == 0) return "";

    // Initialize cache
    let [countT, window] = [{}, {}];
    for (const c of t) {
      countT[c] = c in countT ? countT[c] + 1 : 1;
    }
    let [have, need] = [0, Object.values(countT).reduce((a, b) => a + b)];
    let [str, strLength] = [[-1, -1], Infinity];

    let l = 0;
    for (let r = 0; r < s.length; r++) {
      const c = s[r];
      window[c] = c in window ? window[c] + 1 : 1;

      if (c in countT && window[c] === countT[c]) have += 1;

      while (have === need) {
        // Check if we found smaller substring
        const currStrLength = r - l + 1;
        if (currStrLength < strLength) {
          str = [l, r];
          strLength = currStrLength;
        }
        // Move left pointer and decrement from cache as needed
        window[s[l]] -= 1;
        if (s[l] in countT && window[s[l]] < countT[s[l]]) have -= 1;
        l += 1;
      }
    }

    const [p1, p2] = str;
    return strLength !== Infinity ? s.slice(p1, p2 + 1) : "";
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
