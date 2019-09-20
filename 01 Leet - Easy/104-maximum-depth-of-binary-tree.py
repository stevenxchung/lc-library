'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
'''


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printTree(self):
        print('--- Printing binary tree using preorder DFS')
        self._preorderDFS(self)
        print()

    def _preorderDFS(self, node):
        if node:
            print(node.data, end=' ')
            self._preorderDFS(node.left)
            self._preorderDFS(node.right)

head = Node(3)
head.left = Node(9)
head.right = Node(20)
head.right.left = Node(15)
head.right.right = Node(7)
head.printTree()