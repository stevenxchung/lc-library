'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from 'JFK', thus, the itinerary must begin with 'JFK'. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary ['JFK', 'LGA'] has a smaller lexical order than ['JFK', 'LGB'].

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
'''
import collections
from time import time
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list with reverse sorted input
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += (b,)
        route = []

        # Find end node first and backtrack
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')

        return route[::-1]

    def reference(self, tickets: List[List[str]]) -> List[str]:
        res = ['JFK']
        adj = {k[0]: collections.deque() for k in tickets}
        # Build adjacency list based on alphabetical order
        tickets.sort()
        for a, b in tickets:
            adj[a].append(b)

        def dfs(airport):
            # Add +1 since we start with JFK in list
            if len(res) == len(tickets) + 1:
                return True
            if airport not in adj:
                return False

            temp = list(adj[airport])
            for v in temp:
                # Take from beginning of list
                adj[airport].popleft()
                res.append(v)
                if dfs(v):
                    return res
                # Backtrack if path has no return
                res.pop()
                adj[airport].append(v)

            return False

        dfs('JFK')
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findItinerary(case))
                else:
                    self.findItinerary(case)
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
        [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']],
        [
            ['JFK', 'SFO'],
            ['JFK', 'ATL'],
            ['SFO', 'ATL'],
            ['ATL', 'JFK'],
            ['ATL', 'SFO'],
        ],
    ]
    test.quantify(test_cases)
