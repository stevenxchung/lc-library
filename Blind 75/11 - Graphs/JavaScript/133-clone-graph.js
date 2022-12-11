const { performance } = require('perf_hooks');

class Node {
  constructor(val, neighbors) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

class Solution {
  method(node) {
    if (!node) return null;

    let nodeMap = new Map();

    const dfs = (inputNode) => {
      if (nodeMap.has(inputNode)) return nodeMap.get(inputNode);

      const newNode = new Node(inputNode.val);
      nodeMap.set(inputNode, newNode);
      for (let n of inputNode.neighbors) {
        newNode.neighbors.push(dfs(n));
      }

      return newNode;
    };

    return dfs(node);
  }

  reference(node, seen = new Map()) {
    const isBaseCase = node === null;
    if (isBaseCase) return null;

    if (seen.has(node)) return seen.get(node);

    return this.dfs(node, seen);
  }

  dfs = (node, seen) => {
    const clone = new Node(node.val);

    seen.set(node, clone); /*               | Space O(N) */

    for (const neighbor of node.neighbors) {
      const cloneNeighbor = this.reference(
        neighbor,
        seen
      ); /* Time O(V + E) | Space O(H) */

      clone.neighbors.push(cloneNeighbor); /*               | Space O(V + E) */
    }

    return clone;
  };

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
const node1 = new Node(1);
const node2 = new Node(2);
const node3 = new Node(3);
const node4 = new Node(4);
node1.neighbors = [node2, node4];
node2.neighbors = [node1, node3];
node3.neighbors = [node2, node4];
node4.neighbors = [node1, node3];
const testCases = [node1, new Node(1), null];
test.quantify(testCases);
