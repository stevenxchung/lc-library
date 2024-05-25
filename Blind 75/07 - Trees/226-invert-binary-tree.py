'''
Given the root of a binary tree, invert the tree, and return its root.
'''

from time import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return

            node.left, node.right = dfs(node.right), dfs(node.left)

            return node

        return dfs(root)

    def reference(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.reference(root.left)
        self.reference(root.right)
        return root

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.invertTree(case))
                else:
                    self.invertTree(case)
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
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        ),
        TreeNode(2, TreeNode(1), TreeNode(3)),
        None,
    ]
    test.quantify(test_cases)
