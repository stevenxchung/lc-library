'''
Given a binary tree, flatten it to a linked list in-place.
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Using preorder DFS
    def printTree(self):
        node = self
        if node is None:
            return

        stack = []
        stack.append(node)
        print('Preorder DFS:', end=' ')
        while len(stack) > 0:
            node = stack.pop()
            print(node.val, end=' ')

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)


class Solution:
    def __init__(self):
        # This will be used to reference to the previous node branch
        self.prev = None

    def flatten(self, node):
        if node is None:
            return
        # Since we want to branch right, start with right first then left
        self.flatten(node.right)
        self.flatten(node.left)

        # Right of current node becomes prev node branch
        node.right = self.prev
        node.left = None
        # Set prev node branch to equal current node
        self.prev = node


# Test
# node2 = Node(2, Node(3), Node(4))
# node5 = Node(5, None, Node(6))
# head = Node(1, node2, node5)
# head.printTree()  # 1, 2, 3, 4, 5, 6

head = Node(1, Node(3), Node(4))
head.printTree()  # 1, 3, 4

# Test flatten()
sol = Solution()
sol.flatten(head)
