'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
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
