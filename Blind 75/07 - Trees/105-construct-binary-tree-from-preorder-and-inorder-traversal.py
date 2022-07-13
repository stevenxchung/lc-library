'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''
from time import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        i = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[i])
        root.left = self.buildTree(preorder, inorder[:i])
        root.right = self.buildTree(preorder, inorder[i + 1:])

        return root

    def reference(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.reference(preorder[1:mid + 1], inorder[:mid])
        root.right = self.reference(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.buildTree(case[0], case[1]))
                else:
                    self.buildTree(case[0], case[1])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1]))
                else:
                    self.reference(case[0], case[1])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7]
        ),
        (
            [-1],
            [-1]
        )
    ]
    test.quantify(test_cases)
