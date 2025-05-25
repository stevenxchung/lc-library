'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

from math import inf
from time import time
from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        # Ensure that length of nums1 < nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = nums1, nums2
        n1_len, n2_len = len(nums1), len(nums2)
        half = (n1_len + n2_len) // 2

        l, r = 0, n1_len - 1
        while True:
            # Midpoint for both arrays
            i = l + ((r - l) // 2)
            # Partition where (i + 1) + (j + 1) = half
            j = half - i - 2

            # Initialize left and right values for both arrays
            n1_L = n1[i] if i >= 0 else -inf
            n1_R = n1[i + 1] if i + 1 < n1_len else inf
            n2_L = n2[j] if j >= 0 else -inf
            n2_R = n2[j + 1] if j + 1 < n2_len else inf

            # Check around midpoints
            if n1_L <= n2_R and n2_L <= n1_R:
                # Even result, otherwise odd
                return (
                    (max(n1_L, n2_L) + min(n1_R, n2_R)) / 2
                    if (n1_len + n2_len) % 2 == 0
                    else min(n1_R, n2_R)
                )
            elif n1_L > n2_R:
                r = i - 1
            else:
                l = i + 1

    def reference(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if (j + 1) < len(B) else float('infinity')

            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd
                if total % 2:
                    return min(Aright, Bright)
                # Even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findMedianSortedArrays(*case))
                else:
                    self.findMedianSortedArrays(*case)
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
    test_cases = [([1, 3], [2]), ([1, 2], [3, 4])]
    test.quantify(test_cases)
