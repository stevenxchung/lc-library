const { performance } = require("perf_hooks");

class Solution {
  method(matrix) {
    let [l, r] = [0, matrix.length - 1];

    while (l < r) {
      for (let i = 0; i < r - l; i++) {
        let [top, bottom] = [l, r];
        let topLeft = matrix[top][l + i];
        matrix[top][l + i] = matrix[bottom - i][l];
        matrix[bottom - i][l] = matrix[bottom][r - i];
        matrix[bottom][r - i] = matrix[top + i][r];
        matrix[top + i][r] = topLeft;
      }

      r -= 1;
      l += 1;
    }

    return matrix;
  }

  reference(matrix) {
    this.transpose(matrix);
    this.reflect(matrix);

    return matrix;
  }

  transpose = function (matrix) {
    let n = matrix.length;
    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        let temp = matrix[j][i];
        matrix[j][i] = matrix[i][j];
        matrix[i][j] = temp;
      }
    }
  };

  reflect = function (matrix) {
    let n = matrix.length;
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n / 2; j++) {
        let temp = matrix[i][j];
        matrix[i][j] = matrix[i][n - j - 1];
        matrix[i][n - j - 1] = temp;
      }
    }
  };

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
  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ],
  [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16],
  ],
];
test.quantify(testCases);
