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

  insert(word) {
    let node = this.root;
    for (const c of word) {
      if (!(c in node.children)) node.children[c] = new TrieNode();
      node = node.children[c];
    }
    node.isEnd = true;
  }

  search(word) {
    let node = this.root;
    for (const c of word) {
      if (!(c in node.children)) {
        if (this.debug) console.log(`search(): ${node.isEnd}`);
        return node.isEnd;
      }
      node = node.children[c];
    }
    if (this.debug) console.log(`search(): ${node.isEnd}`);
    return node.isEnd;
  }

  startsWith(prefix) {
    let node = this.root;
    for (const c of prefix) {
      if (!(c in node.children)) {
        if (this.debug) console.log(`startsWith(): ${false}`);
        return false;
      }
      node = node.children[c];
    }
    if (this.debug) console.log(`startsWith(): ${true}`);
    return true;
  }
}

const test = new Solution((debug = true));
const solStart = performance.now();
test.insert("apple");
test.search("apple"); // return true
test.search("app"); // return false
test.startsWith("app"); // return true
test.insert("app");
test.search("app"); // return true
console.log(`Runtime for solution: ${(performance.now() - solStart) / 1000}`);
