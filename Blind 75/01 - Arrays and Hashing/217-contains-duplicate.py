'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
from time import time


class Solution:
    def containsDuplicate(self, nums) -> bool:
        table = {}
        for e in nums:
            if e not in table:
                table[e] = 1
            elif e in table:
                return True
        return False

    def reference(self, nums) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]

    sol_start = time()
    for case in test_cases:
        print(test.containsDuplicate(case))
    print(f'Runtime for our solution: {time() - sol_start}')

    ref_start = time()
    for case in test_cases:
        print(test.reference(case))
    print(f'Runtime for reference: {time() - ref_start}')
