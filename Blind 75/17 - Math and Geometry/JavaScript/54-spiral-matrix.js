const { performance } = require("perf_hooks");

class Solution {
  method(matrix) {
    let res = [];
    let [top, bottom] = [0, matrix.length];
    let [left, right] = [0, matrix[0].length];
    while (left < right && top < bottom) {
      for (let i = left; i < right; i++) {
        res.push(matrix[top][i]);
      }
      top += 1;

      for (let i = top; i < bottom; i++) {
        res.push(matrix[i][right - 1]);
      }
      right -= 1;

      if (!(left < right && top < bottom)) break;

      for (let i = right - 1; i > left - 1; i--) {
        res.push(matrix[bottom - 1][i]);
      }
      bottom -= 1;

      for (let i = bottom - 1; i > top - 1; i--) {
        res.push(matrix[i][left]);
      }
      left += 1;
    }

    return res;
  }

  reference(matrix, order = []) {
    const [rows, cols] = [matrix.length, matrix[0].length];
    const cells = rows * cols;
    let [top, bot, left, right] = [0, rows - 1, 0, cols - 1];

    while (order.length < cells) {
      /* Time O(ROWS * COLS) */
      this.traverse(
        matrix,
        top,
        bot,
        left,
        right,
        order
      ); /* Time O(ROWS * COLS) | Ignore Auxilary Spsace O(ROWS * COLS) */

      top++;
      bot--;
      left++;
      right--;
    }

    return order;
  }

  traverse = (matrix, top, bot, left, right, order) => {
    this.addTop(
      matrix,
      top,
      bot,
      left,
      right,
      order
    ); /* Time O(COLS) | Ignore Auxilary Spsace O(ROWS * COLS) */
    this.addRight(
      matrix,
      top,
      bot,
      left,
      right,
      order
    ); /* Time O(ROWS) | Ignore Auxilary Spsace O(ROWS * COLS)*/
    this.addBot(
      matrix,
      top,
      bot,
      left,
      right,
      order
    ); /* Time O(COLS) | Ignore Auxilary Spsace O(ROWS * COLS)*/
    this.addLeft(
      matrix,
      top,
      bot,
      left,
      right,
      order
    ); /* Time O(ROWS) | Ignore Auxilary Spsace O(ROWS * COLS. */
  };

  addTop = (matrix, top, bot, left, right, order) => {
    for (let col = left; col <= right; col++) {
      /* Time O(COLS) */
      order.push(matrix[top][col]); /* Ignore Auxilary Spsace O(ROWS * COLS) */
    }
  };

  addRight = (matrix, top, bot, left, right, order) => {
    for (let row = top + 1; row <= bot; row++) {
      /* Time O(ROWS) */
      order.push(
        matrix[row][right]
      ); /* Ignore Auxilary Spsace O(ROWS * COLS) */
    }
  };

  addBot = (matrix, top, bot, left, right, order) => {
    for (let col = right - 1; left <= col; col--) {
      /* Time O(COLS) */
      const isOutOfBounds = top === bot;
      if (isOutOfBounds) return;

      order.push(matrix[bot][col]); /* Ignore Auxilary Spsace O(ROWS * COLS) */
    }
  };

  addLeft = (matrix, top, bot, left, right, order) => {
    for (let row = bot - 1; row >= top + 1; row--) {
      /* Time O(ROWS) */
      const isOutOfBounds = left === right;
      if (isOutOfBounds) return;

      order.push(matrix[row][left]); /* Ignore Auxilary Spsace O(ROWS * COLS) */
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
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
  ],
];
test.quantify(testCases);
