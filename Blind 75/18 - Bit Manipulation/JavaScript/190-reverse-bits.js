const { performance } = require("perf_hooks");

class Solution {
  method(n) {
    let res = 0;
    let count = 32;

    while (count--) {
      res *= 2;
      res += n & 1;
      n = n >> 1;
    }
    return res;
  }

  reference(n, bit = 0) {
    for (let i = 0; i < 32; i++) {
      bit <<= 1; // Double * 2
      bit |= n & 1; // Flip
      n >>= 1; // Reduce * 0.5
    }

    return bit >>> 0;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(input));
        else this.method(input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
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
  parseInt("00000010100101000001111010011100", 2),
  parseInt("11111111111111111111111111111101", 2),
];
test.quantify(testCases);
