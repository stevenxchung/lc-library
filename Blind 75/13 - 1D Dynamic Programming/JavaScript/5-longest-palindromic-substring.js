const { performance } = require('perf_hooks');

class Solution {
  method(s) {
    let longest = '';
    for (let i = 0; i < s.length; i++) {
      if (s.length % 2 !== 0) {
        let [l, r] = [i, i];
        while (l >= 0 && r < s.length && s[l] === s[r]) {
          const temp = s.slice(l, r + 1);
          if (temp.length > longest.length) longest = temp;
          l -= 1;
          r += 1;
        }
      } else {
        let [l, r] = [i, i + 1];
        while (s.length % 2 === 0 && l >= 0 && r < s.length && s[l] === s[r]) {
          const temp = s.slice(l, r + 1);
          if (temp.length > longest.length) longest = temp;
          l -= 1;
          r += 1;
        }
      }
    }

    return longest;
  }

  reference(s) {
    const isEmpty = s.length === 0;
    if (isEmpty) return '';

    const [left, right] = this.search(s); /* Time O(N * N) */

    return s.slice(
      left,
      right + 1
    ); /* Time O(N * N) | Ignore Auxillary Space (N) */
  }

  search = (s, left = 0, right = 0) => {
    for (let index = 0; index < s.length; index++) {
      /* Time O(N) */
      const len1 = this.getLength(s, index, index); /* Time O(N) */
      const len2 = this.getLength(s, index, index + 1); /* Time O(N) */
      const [length, window] = [Math.max(len1, len2), right - left];

      const canSkip = length <= window;
      if (canSkip) continue;

      left = index - ((length - 1) >> 1);
      right = index + (length >> 1);
    }

    return [left, right];
  };

  getLength = (s, left, right) => {
    const canExpand = () => 0 <= left && right < s.length;
    const isSame = () => s[left] === s[right];

    const isPalindrome = () => canExpand() && isSame();
    while (isPalindrome()) {
      left--;
      right++;
    } /* Time O(N) */

    const window = right - left - 1;

    return window;
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
const testCases = ['babad', 'cbbd'];
test.quantify(testCases);
