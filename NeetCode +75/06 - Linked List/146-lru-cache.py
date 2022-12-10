'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
'''
from time import time


class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int, debug=False):
        self.debug = debug
        self.capacity = capacity
        # Consists of {key: Node}
        self.cache = {}
        self.lru, self.mru = Node(), Node()
        self.lru.next, self.mru.prev = self.mru, self.lru

    def remove(self, node: Node):
        # Remove linking
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node: Node):
        # Add to front of list
        prev, next = self.mru.prev, self.mru
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        res = None
        if key in self.cache:
            # Move to front of list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            res = self.cache[key]
            if self.debug:
                print(f'Return: {res.val}')
            return res

        res = -1
        if self.debug:
            print(f'Return: {res}')
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove from list if exists
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove LRU
            lru = self.lru.next
            self.remove(lru)
            if self.debug:
                print(f'Removing LRU: {lru.val}')
            del self.cache[lru.key]


if __name__ == '__main__':
    test = LRUCache(2, debug=True)
    sol_start = time()
    test.put(1, 1)  # Cache is {1=1}
    test.put(2, 2)  # Cache is {1=1, 2=2}
    test.get(1)    # Return 1
    test.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    test.get(2)    # Returns -1 (not found)
    test.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    test.get(1)    # Return -1 (not found)
    test.get(3)    # Return 3
    test.get(4)    # Return 4
    print(f'Runtime for our solution: {time() - sol_start}')
