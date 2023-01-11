'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''
from time import time
from typing import List


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        '''
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        '''
        res = []
        candidates.sort()

        def dfs(target: int, index: int, path: List):
            if target < 0:
                # Backtracking
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(target - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return res

    def reference(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.combinationSum(*case))
                else:
                    self.combinationSum(*case)
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
    test_cases = [([2, 3, 6, 7], 7), ([2, 3, 5], 8), ([2], 1)]
    test.quantify(test_cases)
