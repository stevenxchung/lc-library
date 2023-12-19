'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(-1)
        prev = head

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next, l1 = l1, l1.next
            elif l2.val <= l1.val:
                prev.next, l2 = l2, l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return head.next
