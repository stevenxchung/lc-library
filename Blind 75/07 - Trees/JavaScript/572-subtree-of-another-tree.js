const { performance } = require("perf_hooks");

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class Solution {
  isSameTree(p, q) {
    if (!p && !q) return true;
    if (!p || !q || p.val !== q.val) return false;

    return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
  }

  method(root, subRoot) {
    const dfs = (node, subNode) => {
      if (!node) return false;
      if (this.isSameTree(node, subNode)) return true;

      return dfs(node.left, subNode) || dfs(node.right, subNode);
    };

    return dfs(root, subRoot);
  }

  reference(root, subRoot) {
    if (!root) return false;

    if (this.isSame(root, subRoot)) return true;

    const hasLeftTree = this.reference(root.left, subRoot);
    const hasRightTree = this.reference(root.right, subRoot);

    return hasLeftTree || hasRightTree;
  }

  isSame = (root, subRoot) => {
    const hasReachedEnd = !(root && subRoot);
    if (hasReachedEnd) return root === subRoot;

    const isMismatch = root.val !== subRoot.val;
    if (isMismatch) return false;

    const isLeftSame = this.isSame(root.left, subRoot.left);
    const isRightSame = this.isSame(root.right, subRoot.right);

    return isLeftSame && isRightSame;
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(input[0], input[1]));
        else this.method(input[0], input[1]);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(input[0], input[1]));
        else this.reference(input[0], input[1]);
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
    new TreeNode(
      3,
      new TreeNode(4, new TreeNode(1), new TreeNode(2)),
      new TreeNode(5)
    ),
    new TreeNode(4, new TreeNode(1), new TreeNode(2)),
  ],
  [
    new TreeNode(
      3,
      new TreeNode(4, new TreeNode(1), new TreeNode(2, new TreeNode(0))),
      new TreeNode(5)
    ),
    new TreeNode(4, new TreeNode(1), new TreeNode(2)),
  ],
];
test.quantify(testCases);
