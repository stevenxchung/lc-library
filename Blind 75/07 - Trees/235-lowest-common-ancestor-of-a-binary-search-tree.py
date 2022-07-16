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
    res = None

    def search(self, root, p, q):
        if not root:
            return False
        mid = left = right = False
        if root.val == p.val or root.val == q.val:
            mid = True

        left = self.search(root.left, p, q)
        right = self.search(root.right, p, q)
        if mid:
            if left or right:
                self.res = root
        elif left and right:
            self.res = root
        return mid or left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root

        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node

    def reference(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None

        self.search(root, p, q)
        return self.res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.lowestCommonAncestor(
                        case[0], case[1], case[2]).val)
                else:
                    self.lowestCommonAncestor(case[0], case[1], case[2])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1], case[2]).val)
                else:
                    self.reference(case[0], case[1], case[2])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            TreeNode(6,
                     TreeNode(2,
                              TreeNode(0),
                              TreeNode(4, TreeNode(3), TreeNode(5))),
                     TreeNode(8,
                              TreeNode(7),
                              TreeNode(9)),
                     ),
            TreeNode(2), TreeNode(8)
        ),
        (
            TreeNode(6,
                     TreeNode(2,
                              TreeNode(0),
                              TreeNode(4, TreeNode(3), TreeNode(5))),
                     TreeNode(8,
                              TreeNode(7),
                              TreeNode(9)),
                     ),
            TreeNode(2), TreeNode(4)
        ),
        (
            TreeNode(2, TreeNode(1)),
            TreeNode(2), TreeNode(1)
        ),
        # Additional
        (
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(3), TreeNode(1)
        ),
        (
            TreeNode(3,
                     TreeNode(1, None, TreeNode(2)),
                     TreeNode(4)
                     ),
            TreeNode(2), TreeNode(4)
        ),
    ]
    test.quantify(test_cases)
