'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
from time import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursiveDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(
            self.recursiveDFS(root.left), self.recursiveDFS(root.right)
        )

    def iterativeBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    def iterativeDFS(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        level = 0
        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return level

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.iterativeDFS(root)

    def reference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.recursiveDFS(case))
                else:
                    self.recursiveDFS(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
        TreeNode(2, None, TreeNode(1)),
    ]
    test.quantify(test_cases)
