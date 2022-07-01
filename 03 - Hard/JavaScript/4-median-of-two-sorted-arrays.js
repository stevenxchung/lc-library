/*
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  // Index of median
  iPrev = Math.round(num1.length / 2) - 1
  jPrev = Math.round(num2.length / 2) - 1

  if (nums1[iPrev] > nums2[jPrev]) {
    i = iPrev / 2
    j = Math.round((nums2.length + jPrev) / 2) - 1
  } else {
    i = Math.round((nums1.length + iPrev) / 2) - 1
    j = jPrev / 2
  }

  while () {
    iPrev = i
    jPrev = j

    i = Math.round((i + iPrev)/2) - 1
    j = Math.round((j + jPrev)/2) - 1
  }

  // return (nums1[1] + nums2[0]) / 2;
};

nums1 = [1, 2];
nums2 = [3, 4];

console.log(findMedianSortedArrays(nums1, nums2));
