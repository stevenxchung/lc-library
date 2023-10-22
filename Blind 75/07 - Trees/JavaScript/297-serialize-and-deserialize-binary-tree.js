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
    let res = [];
    const dfs = (node) => {
      if (!node) {
        res.push("N");
        return;
      }
      res.push(node.val.toString());
      dfs(node.left);
      dfs(node.right);
    };

    dfs(root);
    return res.join(",");
  }

  deserialize(data) {
    const dfs = (treeAsString, position) => {
      if (treeAsString[position[0]] === "N") {
        position[0] += 1;
        return null;
      }
      const node = new TreeNode(Number(treeAsString[position[0]]));
      position[0] += 1;
      node.left = dfs(treeAsString, position);
      node.right = dfs(treeAsString, position);

      return node;
    };

    const treeAsString = data.split(",");

    return dfs(treeAsString, [0]);
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
