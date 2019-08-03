/*

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

*/

let array = [-2, 1, -3, 4, -1, 2, 1, -5, 4];

let maxSubArray = function(nums) {
  let n = nums.length;
  let maxSum = nums[0];
    for(let i = 1; i < n; i++) {
      if (nums[i - 1] > 0) {
        nums[i] += nums[i - 1];
        console.log('after', nums)
      }
      maxSum = Math.max(nums[i], maxSum);
    }
    return maxSum;
};

console.log(maxSubArray(array));
