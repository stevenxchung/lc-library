const { performance } = require("perf_hooks");

class Solution {
  method(s, t) {
    if (s.length !== t.length) return false;

    let charCount = {};

    for (let i = 0; i < s.length; i++) {
      charCount[s[i]] = (charCount[s[i]] || 0) + 1;
      charCount[t[i]] = (charCount[t[i]] || 0) - 1;
    }

    for (const k in charCount) {
      if (charCount[k] !== 0) return false;
    }

    return true;
  }

  reference(s, t) {
    if (s.length !== t.length) {
      return false;
    }
    let sMap = {};
    let tMap = {};
    for (let i = 0; i < s.length; i++) {
      if (sMap.hasOwnProperty(s[i])) {
        sMap[s[i]]++;
      } else {
        sMap[s[i]] = 1;
      }
      if (tMap.hasOwnProperty(t[i])) {
        tMap[t[i]]++;
      } else {
        tMap[t[i]] = 1;
      }
    }
    for (let k in sMap) {
      if (sMap[k] !== tMap[k]) {
        return false;
      }
    }
    return true;
  }

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
  ["anagram", "nagaram"],
  ["rat", "car"],
];
test.quantify(testCases);
