const { performance } = require('perf_hooks');

class Solution {
  encode(input) {
    return input.join('#');
  }

  decode(input) {
    let res = [];

    let [l, r] = [0, 0];
    while (r < input.length) {
      while (input[r] !== '#' && r < input.length) {
        // Finds next hash
        r += 1;
      }
      res.push(input.slice(l, r));
      // Set to after last hash
      l = r + 1;
      r = l;
    }

    return res;
  }

  encodeReference(input) {
    return input.map((str) => `${str.length}#${str}`).join('');
  }

  decodeReference(input) {
    const res = [];
    let i = 0;

    while (i < input.length) {
      let j = i;
      while (input[j] !== '#') {
        ++j;
      }

      const len = Number(input.slice(i, j));
      res.push(input.slice(++j, j + len));
      i = j + len;
    }

    return res;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        const encoded = this.encode(input);
        const decoded = this.decode(encoded);
        if (i === 0) console.log(encoded, decoded);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        const encoded = this.encodeReference(input);
        const decoded = this.decodeReference(encoded);
        if (i === 0) console.log(encoded, decoded);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}

const test = new Solution();
const testCases = [
  ['lint', 'code', 'love', 'you'],
  ['we', 'say', ':', 'yes'],
];
test.quantify(testCases);
