'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''

import heapq
from time import time
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int], debug=False):
        self.debug = debug
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        # Limit heap size to k to keep kth largest at top
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add to min heap
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        if self.debug:
            print(f'add({val}): {self.min_heap[0]}')
        return self.min_heap[0]


if __name__ == '__main__':
    test = KthLargest(3, [4, 5, 8, 2], debug=True)
    sol_start = time()
    test.add(3)  # Return 4
    test.add(5)  # Return 5
    test.add(10)  # Return 5
    test.add(9)  # Return 8
    test.add(4)  # Return 8
    print(f'Runtime for our solution: {time() - sol_start}\n')
