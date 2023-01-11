'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''
import collections
from time import time
from typing import List


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # Build list based on generic pattern
                pattern = word[:i] + '*' + word[i + 1 :]
                adj[pattern].append(word)

        seen = set([beginWord])
        q = collections.deque([(beginWord, 1)])
        while q:
            # Pop all nodes in frontier
            for _ in range(len(q)):
                word, steps = q.popleft()
                if word == endWord:
                    return steps
                # Go through each neighbor based on adjacency list
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1 :]
                    for nei in adj[pattern]:
                        if nei not in seen:
                            # Add to queue and increase step if not seen
                            seen.add(nei)
                            q.append((nei, steps + 1))

        return 0

    def reference(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        # Copying for test runs only
        word_list = wordList[:]
        word_list.append(beginWord)
        for word in word_list:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.ladderLength(*case))
                else:
                    self.ladderLength(*case)
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
        ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']),
        ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']),
    ]
    test.quantify(test_cases)
