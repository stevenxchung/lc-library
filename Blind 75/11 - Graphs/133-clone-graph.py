'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
'''
from time import time


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        # Initialize clone and queue with first node
        node_map = {node: Node(node.val)}
        q = [node]
        while q:
            # Set new node
            old = q.pop(0)
            new = node_map[old]

            for nei in old.neighbors:
                # For each neighbor, map old to new node if not exist
                if nei not in node_map:
                    node_map[nei] = Node(nei.val)
                    q.append(nei)
                # Add new neighbors to new node
                new.neighbors.append(node_map[nei])

        return node_map[node]

    def reference(self, node: 'Node') -> 'Node':
        if not node:
            return None

        node_map = {}

        def dfs(node: 'Node'):
            if node in node_map:
                # Return the new node we inserted earlier
                return node_map[node]

            # Create new node and add to hashmap
            node_new = Node(node.val)
            node_map[node] = node_new
            for n in node.neighbors:
                # Recursively add neighbors
                node_new.neighbors.append(dfs(n))

            return node_new

        return dfs(node)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.cloneGraph(case))
                else:
                    self.cloneGraph(case)
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
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]
    test_cases = [node_1, Node(1), None]
    test.quantify(test_cases)
