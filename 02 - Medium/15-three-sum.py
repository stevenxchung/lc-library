'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
'''

# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0]
# nums = [0, 0]
# nums = [1, 2, -2, -1]
# nums = [1, -1, -1, 0]
nums = [3, 0, -2, -1, 1, 2]


class Solution:
    def threeSum(self, nums):
        # Initialize nums as sorted list
        nums = sorted(nums)
        # Initialize set since as set only contains unique triplets
        solSet = set()
        # Check for invalid inputs
        if len(nums) < 3:
            return solSet
        print(nums)
        for i, first in enumerate(nums):
            if i != len(nums) - 1:
                # Initialize pointers
                index2, index3 = i + 1, len(nums) - 1
            else:
                break
            # Target will be zero
            target = -first
            print(first, index2, index3)
            # Loop until indices match
            while index2 < index3:
                twoSum = nums[index2] + nums[index3]
                if target > twoSum:
                    index2 += 1
                elif target < twoSum:
                    index3 -= 1
                else:
                    solSet.add((first, nums[index2], nums[index3]))
                    index2 += 1
                    index3 -= 1

        return solSet


sol = Solution()
print(sol.threeSum(nums))
