'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
from time import time
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for e in nums:
            if e not in table:
                table[e] = 1
            elif e in table:
                table[e] += 1

        # Reverse key-value mapping
        reversed_table = {}
        for key, val in table.items():
            reversed_table[val] = key

        output = set()
        # The max possible frequency is proportional to input length
        max_freq = len(nums)
        for i in range(max_freq, -1, -1):
            if max_freq in reversed_table and len(output) < k:
                output.add(reversed_table[max_freq])
                del reversed_table[max_freq]
            max_freq -= 1

        return output

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

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.topKFrequent(case[0], case[1]))
                else:
                    self.topKFrequent(case[0], case[1])
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
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1)
    ]
    test.quantify(test_cases)
