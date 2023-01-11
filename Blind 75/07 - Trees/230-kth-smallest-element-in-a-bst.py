'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''
from time import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, kth = [0], [0]

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            kth[0] += 1
            if kth[0] == k:
                res[0] = node.val
                return
            dfs(node.right)

        dfs(root)
        return res[0]

    def reference(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.kthSmallest(*case))
                else:
                    self.kthSmallest(*case)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1),
        (
            TreeNode(
                5,
                TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                TreeNode(6),
            ),
            3,
        ),
    ]
    test.quantify(test_cases)
