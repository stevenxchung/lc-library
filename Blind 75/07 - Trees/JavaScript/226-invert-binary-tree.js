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
    const dfs = (node) => {
      if (!node) return null;

      [node.right, node.left] = [dfs(node.left), dfs(node.right)];

      return node;
    };

    return dfs(root);
  }

  reference(root) {
    const isBaseCase = root === null;
    if (isBaseCase) return root;

    return this.dfs(root);
  }

  dfs = (root) => {
    const left = this.reference(root.left);
    const right = this.reference(root.right);

    root.left = right;
    root.right = left;

    return root;
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
  new TreeNode(
    4,
    new TreeNode(2, new TreeNode(1), new TreeNode(3)),
    new TreeNode(7, new TreeNode(6), new TreeNode(9))
  ),
  new TreeNode(2, new TreeNode(1), new TreeNode(3)),
  null,
];
test.quantify(testCases);
