'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric
'''


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printTree(self):
        print('--- Printing tree with preorder DFS ---')
        self._preorderDFS(self)
        print()

    def _preorderDFS(self, node):
        if node:
            print(node.data, end=' ')
            self._preorderDFS(node.left)
            self._preorderDFS(node.right)


left = Node(2)
left.left = Node(3)
left.right = Node(4)
right = Node(2)
right.right = Node(3)
right.left = Node(4)
node1 = Node(1, left, right)
node1.printTree()
