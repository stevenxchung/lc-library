'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
from math import inf
from time import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def valid(self, node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False

        # Pass down parent value as well
        return self.valid(node.left, left, node.val) and self.valid(
            node.right, node.val, right
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, -inf, inf)

    def reference(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isValidBST(case))
                else:
                    self.isValidBST(case)
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
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))),
        # Additional
        TreeNode(),
        TreeNode(1, TreeNode(1)),
    ]
    test.quantify(test_cases)
