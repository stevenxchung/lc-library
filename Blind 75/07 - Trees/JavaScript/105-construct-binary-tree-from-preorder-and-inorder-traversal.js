const { performance } = require('perf_hooks');

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class Solution {
  method(preorder, inorder) {
    if (preorder.length === 0 || inorder.length === 0) return null;

    const i = inorder.indexOf(preorder.shift());
    let root = new TreeNode(inorder[i]);
    root.left = this.method(preorder, inorder.slice(0, i));
    root.right = this.method(preorder, inorder.slice(i + 1));

    return root;
  }

  reference(preorder, inorder) {
    const isBaseCase = !preorder.length || !inorder.length;
    if (isBaseCase) return null;

    const { leftInorder, mid, rightInorder } = this.getPointers(
      preorder,
      inorder
    );
    const root = new TreeNode(inorder[mid]);

    root.left = this.reference(preorder, leftInorder);
    root.right = this.reference(preorder, rightInorder);

    return root;
  }

  getPointers = (preorder, inorder) => {
    const next = preorder.shift();
    const mid = inorder.indexOf(next);
    const leftInorder = inorder.slice(0, mid);
    const rightInorder = inorder.slice(mid + 1);

    return { leftInorder, mid, rightInorder };
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.method(copy[0], copy[1]));
        else this.method(copy[0], copy[1]);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.reference(copy[0], copy[1]));
        else this.reference(copy[0], copy[1]);
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
    [3, 9, 20, 15, 7],
    [9, 3, 15, 20, 7],
  ],
  [[-1], [-1]],
];
test.quantify(testCases);
