'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
from time import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(0, head)
        p1, p2 = node, head
        # Adjust gap between pointers
        for i in range(n):
            p2 = p2.next

        while p2:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next

        return node.next

    def reference(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # Delete
        left.next = left.next.next
        return dummy.next

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.removeNthFromEnd(case[0], case[1]))
                else:
                    self.removeNthFromEnd(case[0], case[1])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1]))
                else:
                    self.reference(case[0], case[1])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
        (ListNode(1), 1),
        (ListNode(1, ListNode(2)), 1),
    ]
    test.quantify(test_cases)
