'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''


class Solution:
    def containsDuplicate(self, nums) -> bool:
        table = {}
        for e in nums:
            if e not in table:
                table[e] = 1
            elif e in table:
                return True
        return False


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]

    for case in test_cases:
        print(test.containsDuplicate(case))
