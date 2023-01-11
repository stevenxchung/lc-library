'''
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
'''
from time import time
from typing import List


class Solution:
    def carFleet(
        self, target: int, position: List[int], speed: List[int]
    ) -> int:
        # A car in front always remains ahead and car in back always remains behind
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)

        # Stack to capture unique number of fleets
        stack = []
        for x, x_prime in arr:
            # Time it takes to get to target given position and speed
            t = (target - x) / x_prime
            # When stack is empty or car behind slower than car in front
            if len(stack) == 0 or t > stack[-1]:
                stack.append(t)

        return len(stack)

    def reference(
        self, target: int, position: List[int], speed: List[int]
    ) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.carFleet(*case))
                else:
                    self.carFleet(*case)
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
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
        (10, [3], [3]),
        (100, [0, 2, 4], [4, 2, 1]),
    ]
    test.quantify(test_cases)
