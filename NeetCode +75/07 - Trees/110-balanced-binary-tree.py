'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

A binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
from time import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode]):
            if not node:
                return [True, 0]

            l_bool, l_height = dfs(node.left)
            r_bool, r_height = dfs(node.right)

            is_balanced = l_bool and r_bool \
                and abs(l_height - r_height) <= 1
            height = 1 + max(l_height, r_height)

            return [is_balanced, height]

        return dfs(root)[0]

    def reference(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isBalanced(case))
                else:
                    self.isBalanced(case)
        print(f'Runtime for our solution: {time() - sol_start}')

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
        TreeNode(3,
                 TreeNode(9),
                 TreeNode(20, TreeNode(15), TreeNode(7))
                 ),
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(3, TreeNode(4), TreeNode(4)),
                          TreeNode(3)
                          ),
                 TreeNode(2)
                 ),
        None
    ]
    test.quantify(test_cases)
