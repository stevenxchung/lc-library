'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
'''
import collections
from time import time
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # Monotonically decreasing queue
        index_queue = []
        l = r = 0
        while r < len(nums):
            # Remove smaller values from queue
            while index_queue and nums[index_queue[-1]] < nums[r]:
                index_queue.pop()
            index_queue.append(r)

            # Remove first element if outside window
            if l > index_queue[0]:
                index_queue.pop(0)

            # Add if window has k elements
            if (r + 1) >= k:
                res.append(nums[index_queue[0]])
                l += 1
            r += 1

        return res

    def reference(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # Index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # Pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxSlidingWindow(*case))
                else:
                    self.maxSlidingWindow(*case)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [([1, 3, -1, -3, 5, 3, 6, 7], 3), ([1], 1)]
    test.quantify(test_cases)
