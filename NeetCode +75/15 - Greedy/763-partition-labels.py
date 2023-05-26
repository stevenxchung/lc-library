'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
'''
from time import time
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_i_map = {s[i]: i for i in range(len(s))}
        n, res = 0, []
        # Loop through string for n-partitions
        while n < len(s):
            end, i = last_i_map[s[n]], n + 1
            # Loop to find partition size
            while i < end:
                # Extend partition if character found to occur outside of boundary
                if last_i_map[s[i]] > end:
                    end = last_i_map[s[i]]
                i += 1
            # Add partition size and set to next partition
            res.append(end - n + 1)
            n = end + 1

        return res

    def reference(self, s: str) -> List[int]:
        count = {}
        res = []
        i, length = 0, len(s)
        for j in range(length):
            c = s[j]
            count[c] = j

        curLen = 0
        goal = 0
        while i < length:
            c = s[i]
            goal = max(goal, count[c])
            curLen += 1

            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.partitionLabels(case))
                else:
                    self.partitionLabels(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
        'ababcbacadefegdehijhklij',
        'eccbbbbdec',
        # Additional
        'caedbdedda',
    ]
    test.quantify(test_cases)
