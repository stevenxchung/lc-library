'''

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

'''


class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        # store data
        self.data = data
        # store reference (next item)
        self.next = None

        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.value < l2.value:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

print(ListNode(1).has_value(1))
