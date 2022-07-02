'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
'''


class Solution:
    def fizzBuzz(self, n: int):
        arr = []
        for i in range(1, n+1):
            if i % 15 == 0:
                arr.append('FizzBuzz')
            elif i % 3 == 0:
                arr.append('Fizz')
            elif i % 5 == 0:
                arr.append('Buzz')
            else:
                arr.append(f'{i}')

        print(arr)
        return arr


if __name__ == '__main__':
    test = Solution()
    test_cases = [3, 5, 15]
    for case in test_cases:
        test.fizzBuzz(case)
