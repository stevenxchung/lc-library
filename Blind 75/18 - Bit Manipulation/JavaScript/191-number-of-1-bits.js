const { performance } = require('perf_hooks');

class Solution {
  method(n) {
    let [bits, mask] = [0, 1];

    for (let i = 0; i < 32; i++) {
      const hasBit = (n & mask) !== 0;
      if (hasBit) bits++;

      mask <<= 1;
    }

    return bits;
  }

  reference(n, sum = 0) {
    while (n !== 0) {
      n &= n - 1;
      sum++;
    }

    return sum;
  }

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
  parseInt('00000000000000000000000000001011', 2),
  parseInt('00000000000000000000000010000000', 2),
  parseInt('11111111111111111111111111111101', 2),
];
test.quantify(testCases);
