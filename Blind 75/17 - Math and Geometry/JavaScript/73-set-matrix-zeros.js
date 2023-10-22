const { performance } = require("perf_hooks");

class Solution {
  method(matrix) {
    const [ROWS, COLS] = [matrix.length, matrix[0].length];
    let rowZero = false;

    for (let i = 0; i < ROWS; i++) {
      for (let j = 0; j < COLS; j++) {
        if (matrix[i][j] === 0) {
          matrix[0][j] = 0;
          if (i > 0) matrix[i][0] = 0;
          else rowZero = true;
        }
      }
    }

    for (let i = 1; i < ROWS; i++) {
      for (let j = 1; j < COLS; j++) {
        if (matrix[0][j] === 0 || matrix[i][0] === 0) {
          matrix[i][j] = 0;
        }
      }
    }

    if (matrix[0][0] === 0) {
      for (let i = 0; i < ROWS; i++) {
        matrix[i][0] = 0;
      }
    }

    if (rowZero) {
      for (let j = 0; j < COLS; j++) {
        matrix[0][j] = 0;
      }
    }

    return matrix;
  }

  reference(matrix) {
    const _isColZero = this.isColZero(matrix); /* Time O(ROWS) */

    this.setEdgesToZero(matrix); /* Time O(ROWS) */
    this.setCellsToZero(matrix, _isColZero); /* Time O(ROWS * COLS) */

    return matrix;
  }

  isColZero = (matrix) => matrix.some((row) => row[0] === 0); /* Time O(ROWS) */

  setEdgesToZero = (matrix) => {
    const [rows, cols] = [matrix.length, matrix[0].length];

    for (let row = 0; row < rows; row++) {
      /* Time (ROWS) */
      for (let col = 1; col < cols; col++) {
        /* Time (COLS) */
        const canSet = matrix[row][col] === 0;
        if (!canSet) continue;

        matrix[row][0] = 0;
        matrix[0][col] = 0;
      }
    }
  };

  setCellsToZero = (matrix, isColZero) => {
    const [rows, cols] = [matrix.length, matrix[0].length];

    for (let row = rows - 1; 0 <= row; row--) {
      /* Time (ROWS) */
      for (let col = cols - 1; 1 <= col; col--) {
        /* Time (COLS) */
        if (!this.isZero(matrix, row, col)) continue;

        matrix[row][col] = 0;
      }

      if (isColZero) matrix[row][0] = 0;
    }
  };

  isZero = (matrix, row, col) => {
    const [rowLeftEdge, colTopEdge] = [matrix[row][0], matrix[0][col]];

    return rowLeftEdge === 0 || colTopEdge === 0;
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.method(copy));
        else this.method(copy);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.reference(copy));
        else this.reference(copy);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}

const test = new Solution();
const testCases = [
  //   [
  //     [1, 1, 1],
  //     [1, 0, 1],
  //     [1, 1, 1],
  //   ],
  [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5],
  ],
];
test.quantify(testCases);
