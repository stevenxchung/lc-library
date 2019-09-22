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
        print('--- Printing binary tree using preorder DFS ---')
        self._preorderDFS(self)
        print()

    def printMaxDepth(self):
        # Max depth helper function start with head node at 0 so subtract 1
        print('Maximum depth of binary tree is:', self._maxDepth(self) - 1)

    def _maxDepth(self, node):
        if not node:
            return 0
        else:
            # Continue until leaf node is reached
            leftDepth = self._maxDepth(node.left)
            rightDepth = self._maxDepth(node.right)

        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1

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
head.printMaxDepth()
