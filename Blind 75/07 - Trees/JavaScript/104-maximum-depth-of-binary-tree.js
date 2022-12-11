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
      if (!node) return 0;

      return 1 + Math.max(dfs(node.left), dfs(node.right));
    };

    return dfs(root);
  }

  reference(root) {
    const isBaseCase = root === null;
    if (isBaseCase) return 0;

    return this.bfs([[root, 0]]);
  }

  bfs = (queue, height = 0) => {
    while (queue.length) {
      for (let i = queue.length - 1; 0 <= i; i--) {
        const [root, depth] = queue.shift();

        height = Math.max(height, depth + 1);

        if (root.left) queue.push([root.left, depth + 1]);
        if (root.right) queue.push([root.right, depth + 1]);
      }
    }

    return height;
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
    3,
    new TreeNode(9),
    new TreeNode(20, new TreeNode(15), new TreeNode(7))
  ),
  new TreeNode(2, null, new TreeNode(1)),
];
test.quantify(testCases);
