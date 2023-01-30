'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
from time import time


class Solution:
    def __init__(self):
        self.dic = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dic[n]

    def reference(self, n: int) -> int:
        # Pointers will always be initialized to 1 and 1 during bottom-up
        # as there is only 1 way to land at n when starting at n (0 step) or n - 1 (1 step)
        p1, p2 = 1, 1

        for _ in range(n - 1):
            temp = p1
            p1 += p2
            p2 = temp

        return p1

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.climbStairs(case))
                else:
                    self.climbStairs(case)
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
    test_cases = [2, 3, 4]
    test.quantify(test_cases)
