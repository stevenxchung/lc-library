'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
'''

import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        # Create heap where every parent node is <= child nodes
        heapq.heapify(self.pool)
        # Pops off all elements less than k such that the kth largest will always be self.pool[0]
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        print('List before:', self.pool)
        # Add new value if list is smaller than k
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        # Otherwise value is greater than kth largest, replace
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        print('kth Largest:', self.pool[0])
        print('List after:', self.pool)
        print()
        return self.pool[0]


# Test
k = 4
arr = [4, 5, 8, 2]
kthLargest = KthLargest(k, arr)
kthLargest.add(3)   # Returns 3
kthLargest.add(5)   # Returns 4
kthLargest.add(10)  # Returns 5
kthLargest.add(9)   # Returns 5
kthLargest.add(4)   # Returns 5
