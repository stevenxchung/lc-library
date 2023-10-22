const { performance } = require("perf_hooks");

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class Solution {
  method(root, k) {
    let res = null;

    const dfs = (node, kthSmallest) => {
      if (!node) return;

      dfs(node.left, kthSmallest);
      kthSmallest[0] += 1;
      if (kthSmallest[0] === k) {
        res = node.val;
        return;
      }
      dfs(node.right, kthSmallest);
    };

    dfs(root, [0]);

    return res;
  }

  reference(root, k, stack = []) {
    while (k--) {
      root = this.moveLeft(root, stack);

      const isSmallest = k === 0;
      if (isSmallest) return root.val;

      root = root.right;
    }
  }

  moveLeft = (root, stack) => {
    while (root !== null) {
      stack.push(root);
      root = root.left;
    }

    return stack.pop();
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
  [new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4)), 1],
  [
    new TreeNode(
      5,
      new TreeNode(3, new TreeNode(2, new TreeNode(1)), new TreeNode(4)),
      new TreeNode(6)
    ),
    3,
  ],
];
test.quantify(testCases);
