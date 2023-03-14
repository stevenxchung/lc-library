'''
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [a_i, b_i, c_i] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

- Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)].
- For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].

Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
'''
from time import time
from typing import List


class Solution:
    def mergeTriplets(
        self, triplets: List[List[int]], target: List[int]
    ) -> bool:
        target_placeholder = [0, 0, 0]
        for tri in triplets:
            # Skip triplet if any number is greater than target
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                continue

            # Save numbers that equal target - it's possible to make that combination
            if tri[0] == target[0]:
                target_placeholder[0] = tri[0]
            if tri[1] == target[1]:
                target_placeholder[1] = tri[1]
            if tri[2] == target[2]:
                target_placeholder[2] = tri[2]

        if target_placeholder == target:
            return True

        return False

    def reference(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.mergeTriplets(*case))
                else:
                    self.mergeTriplets(*case)
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
    test_cases = [
        ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]),
        ([[3, 4, 5], [4, 5, 6]], [3, 2, 5]),
        ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]),
    ]
    test.quantify(test_cases)
