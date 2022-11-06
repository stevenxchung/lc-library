'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
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
        q1, q2 = [p], [q]
        while q1 and q2:
            node1, node2 = q1.pop(0), q2.pop(0)
            if (
                node1 and not node2
                or not node1 and node2
                or (node1 and node2 and node1.val != node2.val)
            ):
                return False
            
            if node1:
                q1.append(node1.left)
                q1.append(node1.right)
            if node2:
                q2.append(node2.left)
                q2.append(node2.right)
        
        return True

    def reference(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isSameTree(case[0], case[1]))
                else:
                    self.isSameTree(case[0], case[1])
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
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2), TreeNode(3))
        ),
        (
            TreeNode(1, TreeNode(2)),
            TreeNode(1, None, TreeNode(2))
        ),
        (
            TreeNode(1, TreeNode(2), TreeNode(1)),
            TreeNode(1, TreeNode(1), TreeNode(2))
        )
    ]
    test.quantify(test_cases)
