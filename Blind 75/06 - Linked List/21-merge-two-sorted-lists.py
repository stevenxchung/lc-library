'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
from copy import deepcopy
from time import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        p1 = node
        while list1 and list2:
            if list1.val < list2.val:
                p1.next = list1
                list1 = list1.next
            else:
                p1.next = list2
                list2 = list2.next
            p1 = p1.next

        if list1:
            p1.next = list1
        elif list2:
            p1.next = list2

        return node.next

    def reference(self, list1: Optional[ListNode],
                  list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.mergeTwoLists(copy[0], copy[1]))
                else:
                    self.mergeTwoLists(copy[0], copy[1])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.reference(copy[0], copy[1]))
                else:
                    self.reference(copy[0], copy[1])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4)))
        ),
        (None, None),
        (None, ListNode(0))
    ]
    test.quantify(test_cases)
