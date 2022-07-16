'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.
'''
import heapq
from time import time


class MedianFinder:

    def __init__(self):
        # Max heap and min heap respectively
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Add to max heap first
        heapq.heappush(self.small, -num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            # Transfer max from small list to large list
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            # List is uneven so take from small and push to large
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            # Opposite of above take from large and push to small
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            res = -self.small[0]
            print(res)
            return res
        elif len(self.small) < len(self.large):
            res = self.large[0]
            print(res)
            return res
        # Otherwise take average
        res = float(self.large[0] - self.small[0]) / 2
        print(res)
        return res


if __name__ == '__main__':
    test = MedianFinder()
    sol_start = time()
    test.addNum(1)    # arr = [1]
    test.addNum(2)    # arr = [1, 2]
    test.findMedian()  # return 1.5 (i.e., (1 + 2) / 2)
    test.addNum(3)    # arr[1, 2, 3]
    test.findMedian()  # return 2.0
    print(f'Runtime for our solution: {time() - sol_start}')
