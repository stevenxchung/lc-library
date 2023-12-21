'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Brute force solution
class Solution:
    def mergeKLists(self, lists):
        # Initialize nodes as array to store values
        self.nodes = []
        head = point = ListNode(0)
        # Take all input nodes and append to nodes array
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        # Sort nodes array and link all values
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
