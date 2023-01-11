'''
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
'''
from time import time


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return f'{x ** n:.5f}'

    def reference(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.myPow(*case))
                else:
                    self.myPow(*case)
        print(f'Runtime for our solution: {time() - sol_start}')

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
    test_cases = [(2, 10), (2.1, 3), (2, -2)]
    test.quantify(test_cases)
