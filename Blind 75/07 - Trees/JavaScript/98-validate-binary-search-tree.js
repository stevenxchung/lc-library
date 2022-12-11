const { performance } = require('perf_hooks');

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class Solution {
  method(root) {
    const dfs = (node, left, right) => {
      if (!node) return true;
      if (left >= node.val || right <= node.val) return false;

      return dfs(node.left, left, node.val) && dfs(node.right, node.val, right);
    };

    return dfs(root, -Infinity, Infinity);
  }

  reference(root, min = -Infinity, max = Infinity) {
    const isBaseCase = root === null;
    if (isBaseCase) return true;

    const isInvalid = root.val <= min || max <= root.val;
    if (isInvalid) return false;

    return this.dfs(root, min, max);
  }

  dfs = (root, min, max) => {
    const left = this.reference(root.left, min, root.val);
    const right = this.reference(root.right, root.val, max);

    return left && right;
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
const testCases = [
  new TreeNode(2, new TreeNode(1), new TreeNode(3)),
  new TreeNode(
    5,
    new TreeNode(1),
    new TreeNode(4, new TreeNode(3), new TreeNode(6))
  ),
  // Additional
  new TreeNode(),
  new TreeNode(1, new TreeNode(1)),
];
test.quantify(testCases);
