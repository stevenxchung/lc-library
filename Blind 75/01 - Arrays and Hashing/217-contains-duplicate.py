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

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.containsDuplicate(case))
                else:
                    self.containsDuplicate(case)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]
    test.quantify(test_cases)
