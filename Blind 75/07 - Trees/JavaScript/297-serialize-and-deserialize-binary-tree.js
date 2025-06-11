const { performance } = require("perf_hooks");

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class Solution {
  serialize(root) {
    const res = [];

    const dfs = (node) => {
      if (!node) {
        res.push(null);
        return;
      }
      res.push(node.val);
      dfs(node.left);
      dfs(node.right);

      return;
    };

    dfs(root);
    return JSON.stringify(res);
  }

  deserialize(data) {
    const vals = JSON.parse(data);

    const dfs = () => {
      if (vals.length === 0) return null;

      const val = vals.shift();
      if (val === null) return null;

      const node = new TreeNode(val);
      node.left = dfs();
      node.right = dfs();

      return node;
    };

    return dfs();
  }

  serializeReference(root, result = []) {
    this.serial(root, result);

    return result;
  }

  serial = (root, result) => {
    const isBase = root === null;
    if (isBase) return result.push(null);

    this.dfsSerialize(root, result);
  };

  dfsSerialize = (node, result) => {
    result.push(node.val);
    this.serial(node.left, result);
    this.serial(node.right, result);
  };

  deserializeReference(data) {
    const isBaseCase = !data.length;
    if (isBaseCase) return null;

    const val = data.shift();

    const isNull = val === null;
    if (isNull) return null;

    return this.dfsDeserialize(val, data);
  }

  dfsDeserialize = (val, data) => {
    const node = new TreeNode(val);

    node.left = this.deserializeReference(data);
    node.right = this.deserializeReference(data);

    return node;
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        const serialized = this.serialize(input);
        const tree = this.deserialize(serialized);
        if (i === 0) console.log(serialized, tree);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        const serialized = this.serializeReference(input);
        const tree = this.deserializeReference(serialized);
        if (i === 0) console.log(serialized, tree);
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
    1,
    new TreeNode(2),
    new TreeNode(3, new TreeNode(4), new TreeNode(5))
  ),
  null,
];
test.quantify(testCases);
