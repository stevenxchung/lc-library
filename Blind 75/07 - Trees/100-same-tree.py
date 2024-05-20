'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

from collections import deque
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
        if (not p and q) or (p and not q):
            return False

        q1, q2 = deque([p]), deque([q])
        while q1 and q2:
            node1, node2 = q1.popleft(), q2.popleft()

            if (
                node1.val != node2.val
                or (not node1.left and node2.left)
                or (node1.left and not node2.left)
                or (not node1.right and node2.right)
                or (node1.right and not node2.right)
            ):
                return False

            if node1.left and node2.left:
                q1.append(node1.left)
                q2.append(node2.left)
            if node1.right and node2.right:
                q1.append(node1.right)
                q2.append(node2.right)

        return True

    def reference(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(
            p.right, q.right
        )

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isSameTree(*case))
                else:
                    self.isSameTree(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
        (
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2), TreeNode(3)),
        ),
        (TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))),
        (
            TreeNode(1, TreeNode(2), TreeNode(1)),
            TreeNode(1, TreeNode(1), TreeNode(2)),
        ),
    ]
    test.quantify(test_cases)
