const { performance } = require('perf_hooks');

class Solution {
  method(s) {
    const alphaSuffixes = '0123456';
    let cache = {};
    cache[`${s.length}`] = 1;

    for (let i = s.length - 1; i >= 0; i--) {
      if (s[i] === '0') cache[i] = 0;
      else cache[i] = cache[i + 1];

      if (
        (i + 1 < s.length && s[i] === '1') ||
        (s[i] === '2' && alphaSuffixes.includes(s[i + 1]))
      ) {
        cache[i] += cache[i + 2];
      }
    }

    return cache[0];
  }

  reference(s) {
    const isBaseCase = !s.length || s[0] === '0';
    if (isBaseCase) return 0;

    return this.decode(s);
  }

  decode = (s) => {
    let [prev, prevPrev] = [1, 1];

    for (let curr = 1; curr < s.length; curr++) {
      const temp = prev;

      const isEqual = s[curr] === '0';
      if (isEqual) prev = 0;

      if (this.isTwoDigit(s, curr)) prev += prevPrev;

      prevPrev = temp;
    }

    return prev;
  };

  isTwoDigit = (s, i) => {
    const [prevChar, curChar] = [s[i - 1], s[i]];
    const is10 = prevChar === '1';
    const is20 = prevChar === '2' && curChar <= '6';

    return is10 || is20;
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
  '12',
  '226',
  '06',
  // Additional
  '101',
  '888',
];
test.quantify(testCases);
