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
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            # Remove minium value
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add to min heap
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # Kth largest is always on the top
        return self.min_heap[0]


if __name__ == '__main__':
    test = KthLargest(3, [4, 5, 8, 2])
    sol_start = time()
    test.add(3)  # return 4
    test.add(5)  # return 5
    test.add(10)  # return 5
    test.add(9)  # return 8
    test.add(4)  # return 8
    print(f'Runtime for our solution: {time() - sol_start}\n')
