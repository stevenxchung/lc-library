'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

from copy import deepcopy
from time import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        def dfs(pre, inord):
            if not pre or not inord:
                return None

            node = TreeNode(pre[0])
            # Get inorder node position based on preorder node
            i = inord.index(pre[0])
            # Left of node uses inorder up to node position
            node.left = dfs(pre[1 : i + 1], inord[:i])
            # Right of node uses inorder starting from node position + 1
            node.right = dfs(pre[i + 1 :], inord[i + 1 :])

            return node

        return dfs(preorder, inorder)

    def reference(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.reference(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.reference(preorder[mid + 1 :], inorder[mid + 1 :])

        return root

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.buildTree(*copy).__dict__)
                else:
                    self.buildTree(*copy)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.reference(*copy).__dict__)
                else:
                    self.reference(*copy)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), ([-1], [-1])]
    test.quantify(test_cases)
