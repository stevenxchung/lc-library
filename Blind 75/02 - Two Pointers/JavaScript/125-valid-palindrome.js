const { performance } = require('perf_hooks');

class Solution {
  method(s) {
    // Alphanumeric only and convert to lowercase
    s = s.replace(/[\W_]+/g, '').toLowerCase();
    let [l, r] = [0, s.length - 1];
    while (l < r) {
      if (s[l] !== s[r]) return false;
      l += 1;
      r -= 1;
    }

    return true;
  }

  reference(s) {
    if (!s.length) return true;

    s = s.toLowerCase();

    return this.isValid(s);
  }

  isValid = (s) => {
    let [left, right] = [0, s.length - 1];

    while (left < right) {
      while (left < right && this.isNonAlphaNumeric(s[left])) left++;
      while (left < right && this.isNonAlphaNumeric(s[right])) right--;

      const isSame = s[left] === s[right];
      if (!isSame) return false;

      left++;
      right--;
    }

    return true;
  };

  isNonAlphaNumeric = (char) => {
    const isNonAlpha = char < 'a' || 'z' < char; // a(97) - z(122)
    const isNonNumeric = char < '0' || '9' < char; // 0(48) - 9(57)

    return isNonAlpha && isNonNumeric;
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
const testCases = ['A man, a plan, a canal: Panama', 'race a car', ' '];
test.quantify(testCases);
