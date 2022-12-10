'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''
from time import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(
            p.right, q.right
        )

    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(
            root.right, subRoot
        )

    def reference(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        # Check Edge case
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        return self.reference(root.left, subRoot) or self.reference(
            root.right, subRoot
        )

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isSubtree(case[0], case[1]))
                else:
                    self.isSubtree(case[0], case[1])
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
            TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
            TreeNode(4, TreeNode(1), TreeNode(2)),
        ),
        (
            TreeNode(
                3,
                TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))),
                TreeNode(5),
            ),
            TreeNode(4, TreeNode(1), TreeNode(2)),
        ),
    ]
    test.quantify(test_cases)
