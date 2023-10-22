const { performance } = require("perf_hooks");

class TrieNode {
  constructor() {
    this.children = {};
    // Converts to true once a word is added to the tree
    this.isEnd = false;
  }
}

class Solution {
  constructor(debug = false) {
    this.debug = debug;
    this.root = new TrieNode();
  }

  addWord(word) {
    let node = this.root;
    for (const c of word) {
      if (!(c in node.children)) node.children[c] = new TrieNode();
      node = node.children[c];
    }
    node.isEnd = true;
  }

  search(word) {
    const dfs = (word, start, curr) => {
      let node = curr;

      for (let i = start; i < word.length; i++) {
        const c = word[i];
        if (c === ".") {
          for (const child of Object.values(node.children)) {
            if (dfs(word, i + 1, child)) return true;
            return false;
          }
        } else {
          if (!(c in node.children)) {
            return false;
          }
          node = node.children[c];
        }
      }
      return node.isEnd;
    };

    const res = dfs(word, 0, this.root);
    if (this.debug) console.log(`search(): ${res}`);

    return res;
  }
}

const test = new Solution((debug = true));
const solStart = performance.now();
test.addWord("bad");
test.addWord("dad");
test.addWord("mad");
test.search("pad"); // return false
test.search("bad"); // return true
test.search(".ad"); // return true
test.search("b.."); // return true
console.log(`Runtime for solution: ${(performance.now() - solStart) / 1000}`);
