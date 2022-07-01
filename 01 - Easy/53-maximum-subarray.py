'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        for i in range(1, len(nums)):
            # Only sum if positive, this way we gather the biggest sum
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            # print('array:', nums)
            maxSum = max(nums[i], maxSum)
        return maxSum


input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
print(sol.maxSubArray(input))
