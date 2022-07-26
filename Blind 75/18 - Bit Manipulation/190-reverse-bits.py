'''
Reverse bits of a given 32 bits unsigned integer.

Note:

- Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
'''
from time import time


class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = '0' * (32 - len(n)) + n
        return int(n[::-1], 2)

    def reference(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.reverseBits(case))
                else:
                    self.reverseBits(case)
        print(f'Runtime for our solution: {time() - sol_start}')

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
        int('00000010100101000001111010011100', 2),
        int('11111111111111111111111111111101', 2),
    ]
    test.quantify(test_cases)
