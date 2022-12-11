const { performance } = require('perf_hooks');

class TrieNode {
  constructor() {
    this.children = {};
    this.isEnd = false;
  }
}

class Solution {
  constructor() {
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
        console.log(false);
        return false;
      }
      node = node.children[c];
    }
    console.log(node.isEnd);
    return node.isEnd;
  }

  startsWith(prefix) {
    let node = this.root;
    for (const c of prefix) {
      if (!(c in node.children)) {
        console.log(false);
        return false;
      }
      node = node.children[c];
    }
    console.log(true);
    return true;
  }
}

const test = new Solution();
const solStart = performance.now();
test.insert('apple');
test.search('apple'); // return true
test.search('app'); // return false
test.startsWith('app'); // return true
test.insert('app');
test.search('app'); // return true
console.log(`Runtime for solution: ${(performance.now() - solStart) / 1000}\n`);
