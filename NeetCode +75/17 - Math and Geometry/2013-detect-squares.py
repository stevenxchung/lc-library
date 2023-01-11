'''
You are given a stream of points on the X-Y plane. Design an algorithm that:

- Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
- Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

- DetectSquares() Initializes the object with an empty data structure.
- void add(int[] point) Adds a new point point = [x, y] to the data structure.
- int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
'''
from time import time
from typing import List


class DetectSquares:
    def __init__(self, debug=False):
        # Need at least 2x 2 different points for each
        self.p_count = {}
        self.p_arr = []
        self.debug = debug

    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) not in self.p_count:
            self.p_count[(x, y)] = 1
        else:
            self.p_count[(x, y)] += 1
        self.p_arr.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.p_arr:
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            a = self.p_count[(x, py)]
            b = self.p_count[(px, y)]
            res += a * b

        if self.debug:
            print(res)

        return res


if __name__ == '__main__':
    test = DetectSquares(debug=True)
    sol_start = time()
    test.add([3, 10])
    test.add([11, 2])
    test.add([3, 2])
    test.count([11, 10])  # Return 1
    test.count([14, 8])  # Return 0
    test.add([11, 2])  # Duplicate allowed
    test.add([11, 1])  # Testing, should not add another square
    test.add([3, 1])  # Testing, should not add another square
    test.count([11, 10])  # Return 2
    print(f'Runtime for our solution: {time() - sol_start}\n')
