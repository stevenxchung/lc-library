'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
import collections
from time import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, q = [], [root]
        while q:
            layer_values, next_layer = [], []
            
            for node in q:
                layer_values.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            
            q = next_layer
            res.append(layer_values)
        
        return res

    def reference(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.levelOrder(case))
                else:
                    self.levelOrder(case)
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
        TreeNode(3,
                 TreeNode(9),
                 TreeNode(20, TreeNode(15), TreeNode(7)),
                 ),
        TreeNode(1),
        None,
        # Additional
        TreeNode(1, TreeNode(2)),
        TreeNode(1,
                 TreeNode(2, TreeNode(4)),
                 TreeNode(3, None, TreeNode(5))
                 )
    ]
    test.quantify(test_cases)
