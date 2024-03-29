'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''
from math import inf
from time import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node, prev_val):
            if not node:
                return

            if node.val >= prev_val:
                res[0] += 1
            max_val = max(node.val, prev_val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, -inf)
        return res[0]

    def reference(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.goodNodes(case))
                else:
                    self.goodNodes(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        TreeNode(
            3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5))
        ),
        TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2))),
        TreeNode(1),
    ]
    test.quantify(test_cases)
