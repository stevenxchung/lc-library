const { performance } = require("perf_hooks");

class Solution {
  method(board, word) {
    const [ROWS, COLS] = [board.length, board[0].length];

    const dfs = (r, c, str) => {
      if (str.length === 0) return true;
      if (r < 0 || c < 0 || r >= ROWS || c >= COLS || board[r][c] !== str[0]) {
        return;
      }

      const temp = board[r][c];
      board[r][c] = "#";

      const foundWord =
        dfs(r + 1, c, str.slice(1)) ||
        dfs(r - 1, c, str.slice(1)) ||
        dfs(r, c + 1, str.slice(1)) ||
        dfs(r, c - 1, str.slice(1));

      board[r][c] = temp;

      return foundWord;
    };

    for (let i = 0; i < ROWS; i++) {
      for (let j = 0; j < COLS; j++) {
        if (dfs(i, j, word)) return true;
      }
    }

    return false;
  }

  reference(board, word) {
    for (let row = 0; row < board.length; row++) {
      for (let col = 0; col < board[0].length; col++) {
        if (this.dfs(board, row, col, word, 0)) return true;
      }
    }

    return false;
  }

  dfs = (board, row, col, word, index) => {
    if (index === word.length) return true;
    if (this.isOutOfBound(board, row, col)) return false;
    if (board[row][col] !== word[index]) return false;

    board[row][col] = "*";

    const hasWord = Object.values(this.directions(row, col)).filter(([r, c]) =>
      this.dfs(board, r, c, word, index + 1)
    ).length;

    board[row][col] = word[index];
    return hasWord;
  };

  isOutOfBound = (board, row, col) => {
    const isRowOutOfBound = row < 0 || board.length - 1 < row;
    const isColOutOfBound = col < 0 || board[0].length - 1 < col;
    return isRowOutOfBound || isColOutOfBound;
  };

  directions = (row, col) => ({
    up: [row - 1, col],
    down: [row + 1, col],
    left: [row, col - 1],
    right: [row, col + 1],
  });

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(...input));
        else this.method(...input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(...input));
        else this.reference(...input);
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
    [
      ["A", "B", "C", "E"],
      ["S", "F", "C", "S"],
      ["A", "D", "E", "E"],
    ],
    "ABCCED",
  ],
  [
    [
      ["A", "B", "C", "E"],
      ["S", "F", "C", "S"],
      ["A", "D", "E", "E"],
    ],
    "SEE",
  ],
  [
    [
      ["A", "B", "C", "E"],
      ["S", "F", "C", "S"],
      ["A", "D", "E", "E"],
    ],
    "ABCB",
  ],
];
test.quantify(testCases);
