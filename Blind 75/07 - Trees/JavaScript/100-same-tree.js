const { performance } = require('perf_hooks');

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class Solution {
  method(p, q) {
    const dfs = (p, q) => {
      if (!p && !q) return true;
      if (!p || !q || p.val !== q.val) return false;

      return dfs(p.left, q.left) && dfs(p.right, q.right);
    };

    return dfs(p, q);
  }

  reference(p, q) {
    const isBaseCase = !(p || q);
    if (isBaseCase) return true;

    const isBalanced = p && q;
    if (!isBalanced) return false;

    const isSame = p.val === q.val;
    if (!isSame) return false;

    return this.dfs(p, q);
  }

  dfs = (p, q) => {
    const left = this.reference(p.left, q.left);
    const right = this.reference(p.right, q.right);

    return left && right;
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(input[0], input[1]));
        else this.method(input[0], input[1]);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
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
    new TreeNode(1, new TreeNode(2), new TreeNode(3)),
    new TreeNode(1, new TreeNode(2), new TreeNode(3)),
  ],
  [new TreeNode(1, new TreeNode(2)), new TreeNode(1, null, new TreeNode(2))],
  [
    new TreeNode(1, new TreeNode(2), new TreeNode(1)),
    new TreeNode(1, new TreeNode(1), new TreeNode(2)),
  ],
];
test.quantify(testCases);
