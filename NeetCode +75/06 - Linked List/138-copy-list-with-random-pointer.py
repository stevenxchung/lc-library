'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.
'''
from copy import deepcopy
from time import time
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None: None}
        node = head
        while node:
            copy = Node(node.val)
            node_map[node] = copy
            node = node.next

        node = head
        while node:
            copy = node_map[node]
            copy.next = node_map[node.next]
            copy.random = node_map[node.random]
            node = node.next

        return node_map[head]

    def reference(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.copyRandomList(copy).__dict__)
                else:
                    self.copyRandomList(copy)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.reference(copy).__dict__)
                else:
                    self.reference(copy)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    input1_1 = Node(7)
    input1_2 = Node(13)
    input1_3 = Node(11)
    input1_4 = Node(10)
    input1_5 = Node(1, None)
    input1_1.next = input1_2
    input1_2.next = input1_3
    input1_3.next = input1_4
    input1_4.next = input1_5
    input1_1.random = None
    input1_2.random = input1_1
    input1_3.random = input1_5
    input1_4.random = input1_3
    input1_5.random = input1_1

    input2_1 = Node(1)
    input2_2 = Node(2, None)
    input2_1.next = input2_2
    input2_1.random = input2_2
    input2_2.random = input2_2

    input3_1 = Node(3)
    input3_2 = Node(3)
    input3_3 = Node(3, None)
    input3_1.next = input3_2
    input3_2.next = input3_3
    input3_1.random = None
    input3_2.random = input3_1
    input3_3.random = None

    test_cases = [input1_1, input2_1, input3_1]
    test.quantify(test_cases)
