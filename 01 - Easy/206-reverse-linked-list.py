'''
Reverse a singly linked list.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         while head:
#             temp = head
#             head = head.next
#             temp.next = prev
#             prev = temp
#         return prev

# Recursive
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p


class LinkedList:
    def __init__(self):
        self.head = None

    # Adds node to end of linked list
    def add(self, node):
        node = ListNode(node)
        # Checks if head is null
        if not self.head:
            self.head = node
            return
        # Go through until the last node
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = node

    # Prints linked list
    def traverse(self):
        current = self.head
        while current:
            if current.next:
                print(current.val, end='->')
            else:
                print(current.val)
            current = current.next

    def reverse(self, node):
        if node.next == None:
            self.head = node
            return
        self.reverse(node.next)
        temp = node.next
        temp.next = node
        node.next = None


ll = LinkedList()
ll.add(15)
ll.add(20)
ll.add(25)
ll.add(30)
ll.traverse()
ll.reverse(ll.head)
ll.traverse()
