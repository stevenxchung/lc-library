const { performance } = require("perf_hooks");

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class Solution {
  method(root) {
    const dfs = (node, path) => {
      if (!node) return 0;

      const leftGain = Math.max(dfs(node.left, path), 0);
      const rightGain = Math.max(dfs(node.right, path), 0);
      const currentMax = node.val + leftGain + rightGain;

      path[0] = Math.max(path[0], currentMax);

      return node.val + Math.max(leftGain, rightGain);
    };

    let maxPath = [-Infinity];
    dfs(root, maxPath);

    return maxPath[0];
  }

  reference(root, maxValue = [-Infinity]) {
    this.pathSum(root, maxValue);

    return maxValue[0];
  }

  pathSum = (root, maxValue) => {
    const isBaseCase = root === null;
    if (isBaseCase) return 0;

    return this.dfs(root, maxValue);
  };

  dfs = (node, maxValue) => {
    const left = Math.max(0, this.pathSum(node.left, maxValue));
    const right = Math.max(0, this.pathSum(node.right, maxValue));
    const sum = left + right + node.val;

    maxValue[0] = Math.max(maxValue[0], sum);

    return Math.max(left, right) + node.val;
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
  new TreeNode(1, new TreeNode(2), new TreeNode(3)),
  new TreeNode(
    -10,
    new TreeNode(9),
    new TreeNode(20, new TreeNode(15), new TreeNode(7))
  ),
];
test.quantify(testCases);
