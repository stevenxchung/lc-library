'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''
import heapq
from time import time
from typing import List
from collections import defaultdict


class Twitter:

    def __init__(self, debug=False):
        self.debug = debug
        self.ranking = 0
        # userId -> list of [count, tweetIds]
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.ranking, tweetId])
        self.ranking -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.following[userId].add(userId)
        for followee_id in self.following[userId]:
            if followee_id in self.tweets:
                index = len(self.tweets[followee_id]) - 1
                count, tweetId = self.tweets[followee_id][index]
                heapq.heappush(min_heap,
                               [count, tweetId, followee_id, index - 1])

        while min_heap and len(res) < 10:
            count, tweetId, followee_id, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followee_id][index]
                heapq.heappush(min_heap,
                               [count, tweetId, followee_id, index - 1])

        if self.debug:
            print(res)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


if __name__ == '__main__':
    test = Twitter(debug=True)
    sol_start = time()
    # User 1 posts a new tweet(id = 5)
    test.postTweet(1, 5)
    # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    test.getNewsFeed(1)
    # User 1 follows user 2
    test.follow(1, 2)
    # User 2 posts a new tweet(id=6)
    test.postTweet(2, 6)
    # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5
    test.getNewsFeed(1)
    # User 1 unfollows user 2
    test.unfollow(1, 2)
    # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2
    test.getNewsFeed(1)
    print(f'Runtime for our solution: {time() - sol_start}')
