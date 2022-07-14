'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
'''
from math import inf
from time import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def dfs_helper_serialize(self, node, output):
        if not node:
            output.append('N')
            return
        output.append(str(node.val))
        self.dfs_helper_serialize(node.left, output)
        self.dfs_helper_serialize(node.right, output)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output = []
        self.dfs_helper_serialize(root, output)
        return ','.join(output)

    def dfs_helper_deserialize(self, tree_as_str, position):
        if tree_as_str[position[0]] == 'N':
            position[0] += 1
            return None
        node = TreeNode(int(tree_as_str[position[0]]))
        position[0] += 1
        node.left = self.dfs_helper_deserialize(tree_as_str, position)
        node.right = self.dfs_helper_deserialize(tree_as_str, position)

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_as_str = data.split(',')
        position = [0]

        return self.dfs_helper_deserialize(tree_as_str, position)

    def serialize_reference(self, root: Optional[TreeNode]) -> int:
        return

    def deserialize_reference(self, root: Optional[TreeNode]) -> int:
        return

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    serialize = self.serialize(case)
                    deserialize = self.deserialize(serialize)
                    print(serialize, deserialize)
                else:
                    serialize = self.serialize(case)
                    deserialize = self.deserialize(serialize)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    serialize = self.serialize_reference(case)
                    deserialize = self.deserialize_reference(serialize)
                    print(serialize, deserialize)
                else:
                    serialize = self.serialize_reference(case)
                    deserialize = self.deserialize_reference(deserialize)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Codec()
    test_cases = [
        TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))),
        None
    ]
    test.quantify(test_cases)
