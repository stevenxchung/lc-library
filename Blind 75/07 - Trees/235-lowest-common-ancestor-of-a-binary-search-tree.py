'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
from time import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        def dfs(node, p, q):
            if p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q)
            if p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)

            return node

        return dfs(root, p, q)

    def reference(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        node = root

        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.lowestCommonAncestor(*case).val)
                else:
                    self.lowestCommonAncestor(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case).val)
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            TreeNode(
                6,
                TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
                TreeNode(8, TreeNode(7), TreeNode(9)),
            ),
            TreeNode(2),
            TreeNode(8),
        ),
        (
            TreeNode(
                6,
                TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
                TreeNode(8, TreeNode(7), TreeNode(9)),
            ),
            TreeNode(2),
            TreeNode(4),
        ),
        (TreeNode(2, TreeNode(1)), TreeNode(2), TreeNode(1)),
        # Additional
        (TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(3), TreeNode(1)),
        (
            TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)),
            TreeNode(2),
            TreeNode(4),
        ),
    ]
    test.quantify(test_cases)
