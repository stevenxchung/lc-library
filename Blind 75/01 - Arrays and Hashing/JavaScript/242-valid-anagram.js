const { performance } = require('perf_hooks');

class Solution {
  method(s, t) {
    if (s.length !== t.length) return false;

    let sStore = {};
    let tStore = {};

    for (const [i, c] of [...s].entries()) {
      sStore[s[i]] = s[i] in sStore ? sStore[s[i]] + 1 : 1;
      tStore[t[i]] = t[i] in tStore ? tStore[t[i]] + 1 : 1;
    }
    for (const [k, v] of Object.entries(sStore)) {
      if (sStore[k] !== tStore[k]) return false;
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
  ['anagram', 'nagaram'],
  ['rat', 'car'],
];
test.quantify(testCases);
