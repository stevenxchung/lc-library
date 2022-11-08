'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''
from math import inf
from time import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: Optional[TreeNode], max_path: List[int]) -> int:
        if not node:
            return 0

        # Check subtree max
        left_gain = max(self.helper(node.left, max_path), 0)
        right_gain = max(self.helper(node.right, max_path), 0)
        subtree_max = node.val + left_gain + right_gain

        # Compare paths with current
        max_path[0] = max(max_path[0], subtree_max)

        # Return the max path after split
        return node.val + max(left_gain, right_gain)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = [-inf]
        self.helper(root, max_path)
        return max_path[0]

    def reference(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # Return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxPathSum(case))
                else:
                    self.maxPathSum(case)
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
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(-10, 
                 TreeNode(9), 
                 TreeNode(20, TreeNode(15), TreeNode(7))
                 )
    ]
    test.quantify(test_cases)
