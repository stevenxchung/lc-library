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
    if (!root) {
      return [];
    }

    let res = [];
    let queue = [[root, 0]];

    while (queue.length > 0) {
      const [node, level] = queue.shift();
      if (res[level] !== undefined) {
        res[level].push(node.val);
      } else {
        res[level] = [node.val];
      }

      if (node.left) {
        queue.push([node.left, level + 1]);
      }
      if (node.right) {
        queue.push([node.right, level + 1]);
      }
    }

    return res;
  }

  reference(root, level = 0, levels = []) {
    const isBaseCase = root === null;
    if (isBaseCase) return levels;

    const isLastNode = level === levels.length;
    if (isLastNode) levels.push([]);

    levels[level].push(root.val);

    return this.dfs(root, level, levels);
  }

  dfs = (root, level, levels) => {
    if (root.left) this.reference(root.left, level + 1, levels);
    if (root.right) this.reference(root.right, level + 1, levels);

    return levels;
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
  new TreeNode(1),
  null,
  // Additional
  new TreeNode(1, new TreeNode(2)),
  new TreeNode(
    1,
    new TreeNode(2, new TreeNode(4)),
    new TreeNode(3, null, new TreeNode(5))
  ),
];
test.quantify(testCases);
