'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

from collections import defaultdict
from time import time
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        # Where i = count and max(count) <= len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count_map[n] += 1
        for n, c in count_map.items():
            buckets[c].append(n)

        # Start from the largest bucket
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    # Only add up to k
                    return res

    def reference(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.topKFrequent(*case))
                else:
                    self.topKFrequent(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
    test_cases = [([1, 1, 1, 2, 2, 3], 2), ([1], 1)]
    test.quantify(test_cases)
