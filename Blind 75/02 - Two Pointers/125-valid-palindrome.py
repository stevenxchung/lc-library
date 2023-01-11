'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
from time import time


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_formatted = ''.join(filter(str.isalnum, s)).lower()
        i = 0
        j = len(s_formatted) - 1
        while i < j:
            if s_formatted[i] != s_formatted[j]:
                return False
            i += 1
            j -= 1

        return True

    def reference(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z')
            or ord('a') <= ord(c) <= ord('z')
            or ord('0') <= ord(c) <= ord('9')
        )

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isPalindrome(case))
                else:
                    self.isPalindrome(case)
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
    test_cases = ['A man, a plan, a canal: Panama', 'race a car', ' ']
    test.quantify(test_cases)
