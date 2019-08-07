'''
Reverse a singly linked list.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        return prev
