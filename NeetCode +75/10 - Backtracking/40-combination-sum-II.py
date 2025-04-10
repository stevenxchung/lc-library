'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

from time import time
from typing import List


class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset[:])
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    # Skip if same as previous value or if over target
                    continue
                if total + candidates[j] > target:
                    break
                # Next index cannot be the same so use j + 1
                dfs(j + 1, subset + [candidates[j]], total + candidates[j])

            return

        dfs(0, [], 0)
        return res

    def reference(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(curr, pos, target):
            if target == 0:
                res.append(curr.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(curr, i + 1, target - candidates[i])
                curr.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.combinationSum2(*case))
                else:
                    self.combinationSum2(*case)
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
        ([10, 1, 2, 7, 6, 1, 5], 8),
        ([2, 5, 2, 1, 2], 5),
        # Additional
        ([3, 1, 3, 5, 1, 1], 8),
    ]
    test.quantify(test_cases)
