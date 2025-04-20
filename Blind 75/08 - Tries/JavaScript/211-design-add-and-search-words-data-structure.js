const { performance } = require("perf_hooks");

class TrieNode {
  constructor() {
    this.children = {};
    // Converts to true once a word is added to the tree
    this.isEnd = false;
  }
}

class Solution {
  constructor({ debug = false }) {
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
    const dfs = (i, node) => {
      if (i === word.length) return node.isEnd;

      const c = word[i];
      if (c === ".") {
        for (const childNode of Object.values(node.children)) {
          if (dfs(i + 1, childNode)) return true;
        }
        return false;
      }

      if (!(c in node.children)) return false;

      return dfs(i + 1, node.children[c]);
    };

    const res = dfs(0, this.root);
    if (this.debug) console.log(`search(): ${res}`);
    return res;
  }
}

let test = new Solution({ debug: true });
const solStart = performance.now();
test.addWord("bad");
test.addWord("dad");
test.addWord("mad");
test.search("pad"); // return false
test.search("bad"); // return true
test.search(".ad"); // return true
test.search("b.."); // return true
console.log(`Runtime for solution: ${(performance.now() - solStart) / 1000}\n`);

console.log("\nAdditional testing...");
test = new Solution({ debug: true });
test.addWord("a");
test.addWord("a");
// true, true, false, true, false, false
test.search(".");
test.search("a");
test.search("aa");
test.search("a");
test.search(".a");
test.search("a.");

test.addWord("at");
test.addWord("and");
test.addWord("an");
test.addWord("add");
// true, false
test.search("a");
test.search(".at");

test.addWord("bat");
// true, true, false, false, true, true
test.search(".at");
test.search("an.");
test.search("a.d.");
test.search("b.");
test.search("a.d");
test.search(".");
console.log(`Runtime for solution: ${(performance.now() - solStart) / 1000}`);
