const { performance } = require("perf_hooks");

class TrieNode {
  constructor() {
    this.children = {};
    this.isEnd = false;
  }
}

class TrieNodeRef {
  constructor() {
    this.children = {};
    this.word = "";
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  add(word) {
    let node = this.root;
    for (const c of word) {
      if (!(c in node.children)) node.children[c] = new TrieNode();
      node = node.children[c];
    }

    node.isEnd = true;
  }
}

class TrieRef {
  constructor(words) {
    this.root = new TrieNodeRef();
    words.forEach((word) => this.insert(word));
  }

  /* Time O(N) | Space O(N) */
  insert(word, node = this.root) {
    for (const char of word) {
      const child = node.children[char] || new TrieNodeRef();

      node.children[char] = child;

      node = child;
    }

    node.word = word;
  }

  /* Time O((ROWS * COLS) * (4 * (3 ^ (WORDS - 1)))) | Space O(N) */
  searchBoard(board, node = this.root, words = []) {
    const [rows, cols] = [board.length, board[0].length];

    for (let row = 0; row < rows; row++) {
      for (let col = 0; col < cols; col++) {
        this.dfs(board, row, rows, col, cols, node, words);
      }
    }

    return words;
  }

  dfs(board, row, rows, col, cols, node, words) {
    const char = board[row][col];
    const child = node.children[char] || null;

    if (this.canSkip(char, child)) return;

    node = child;
    this.checkWord(node, words);
    this.backTrack(board, row, rows, col, cols, node, words);
  }

  canSkip(char, child) {
    const hasSeen = char === "#";
    const isMissingChild = !child;

    return hasSeen || isMissingChild;
  }

  checkWord(node, words) {
    if (!node.word.length) return;

    words.push(node.word);
    node.word = "";
  }

  backTrack(board, row, rows, col, cols, node, words) {
    const char = board[row][col];

    board[row][col] = "#";

    for (const [_row, _col] of this.getNeighbors(row, rows, col, cols)) {
      this.dfs(board, _row, rows, _col, cols, node, words);
    }

    board[row][col] = char;
  }

  getNeighbors(row, rows, col, cols) {
    return [
      [row - 1, col],
      [row + 1, col],
      [row, col - 1],
      [row, col + 1],
    ].filter(([_row, _col]) => !this.isOutOfBounds(_row, rows, _col, cols));
  }

  isOutOfBounds(row, rows, col, cols) {
    const isRowOut = row < 0 || rows <= row;
    const isColOut = col < 0 || cols <= col;

    return isRowOut || isColOut;
  }
}

class Solution {
  method(board, words) {
    let trie = new Trie();
    for (const word of words) {
      trie.add(word);
    }

    const [ROWS, COLS] = [board.length, board[0].length];
    let res = new Set();

    const dfs = (r, c, node, word) => {
      if (
        r < 0 ||
        c < 0 ||
        r >= ROWS ||
        c >= COLS ||
        !(board[r][c] in node.children) ||
        board[r][c] === "#"
      ) {
        return;
      }

      word += board[r][c];
      node = node.children[board[r][c]];
      if (node.isEnd) {
        res.add(word);
      }

      const temp = board[r][c];
      board[r][c] = "#";

      dfs(r + 1, c, node, word);
      dfs(r - 1, c, node, word);
      dfs(r, c + 1, node, word);
      dfs(r, c - 1, node, word);

      board[r][c] = temp;
    };

    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        dfs(r, c, trie.root, "", board);
      }
    }

    return [...res];
  }

  reference(board, words) {
    return new TrieRef(words).searchBoard(board);
  }

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
      ["o", "a", "a", "n"],
      ["e", "t", "a", "e"],
      ["i", "h", "k", "r"],
      ["i", "f", "l", "v"],
    ],
    ["oath", "pea", "eat", "rain"],
  ],
  [
    [
      ["a", "b"],
      ["c", "d"],
    ],
    ["abcb"],
  ],
];
test.quantify(testCases);
