const { performance } = require('perf_hooks');

class Solution {
  method(s) {
    let count = 0;

    for (let i = 0; i < s.length; i++) {
      let [l, r] = [i, i];
      while (
        l >= 0 &&
        l < s.length &&
        r >= 0 &&
        r < s.length &&
        s[l] === s[r]
      ) {
        l -= 1;
        r += 1;
        count += 1;
      }
    }

    for (let i = 0; i < s.length; i++) {
      let [l, r] = [i, i + 1];
      while (
        l >= 0 &&
        l < s.length &&
        r >= 0 &&
        r < s.length &&
        s[l] === s[r]
      ) {
        l -= 1;
        r += 1;
        count += 1;
      }
    }

    return count;
  }

  reference(s, count = 0) {
    for (let i = 0; i < s.length; i++) {
      /* Time O(N) */
      const [odd, even] = [i, i + 1];
      /* odd-length: single character center */
      count += this.isPalindromeFromCenter(s, i, odd); /* Time O(N) */
      /* even-length: consecutive characters center */
      count += this.isPalindromeFromCenter(s, i, even); /* Time O(N) */
    }

    return count;
  }

  isPalindromeFromCenter = (s, left, right, count = 0) => {
    const isInBounds = () => 0 <= left && right < s.length;
    while (isInBounds()) {
      /* Time O(N) */
      const isEqual = s[left] === s[right];
      if (!isEqual) break;

      count++;

      left--;
      right++;
    }

    return count;
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
const testCases = ['abc', 'aaa'];
test.quantify(testCases);
