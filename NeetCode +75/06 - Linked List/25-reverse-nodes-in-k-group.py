'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
from copy import deepcopy
from time import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        node = jump = ListNode(0)
        node.next = l = r = head

        while True:
            count = 0
            # Use r to locate the range
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                # If size k satisfied, reverse the inner linked list
                prev, curr = r, l
                for _ in range(k):
                    # Reverse
                    curr.next, prev, curr = prev, curr, curr.next
                # Connect two k-groups
                jump.next, jump, l = prev, l, r
            else:
                return node.next

    def reference(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # Reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.reverseKGroup(*copy).__dict__)
                else:
                    self.reverseKGroup(*copy)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.reference(*copy).__dict__)
                else:
                    self.reference(*copy)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3),
    ]
    test.quantify(test_cases)
