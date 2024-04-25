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
        '''Doubly Linked-list Node'''
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity=1, debug=False):
        '''
        - Use a doubly-linked list
        - Pointer for MRU (most recently used) on right
        - Pointer for LRU (least recently used) on left
        - Check capacity and remove if needed on put()
        - Shift node to MRU on get()
        - Use hashmap to find nodes by key
        '''
        self.debug = debug
        self.capacity = capacity
        self.cache = {}
        self.lru, self.mru = Node(), Node()
        self.lru.next, self.mru.prev = self.mru, self.lru

    def _remove(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev
        # Remove from hashmap
        del self.cache[node.key]

    def _insert(self, node: Node):
        l, r = self.mru.prev, self.mru
        l.next = r.prev = node
        node.prev, node.next = l, r
        # Add to hashmap
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            if self.debug:
                print(f'get({key}): not found: {-1}')
            return -1

        node = self.cache[key]
        # Reposition node next to MRU pointer
        self._remove(node)
        self._insert(node)

        if self.debug:
            print(f'get({key}): {node.val}')
        return node.val

    def put(self, key: int, value: int) -> None:
        if len(self.cache) + 1 > self.capacity:
            # Adding one will overflow so remove LRU
            node = self.lru.next
            self._remove(node)
            if self.debug:
                print(
                    f'put({key, value}): Removing LRU... {(node.key, node.val)}'
                )

        node = Node(key, value)
        self._insert(node)
        if self.debug:
            res = [(k, node.val) for k, node in self.cache.items()]
            print(f'Cache after put({key, value}): {res}\n')


if __name__ == '__main__':
    test = LRUCache(2, debug=True)
    sol_start = time()
    test.put(1, 1)  # Cache is {1=1}
    test.put(2, 2)  # Cache is {1=1, 2=2}
    test.get(1)  # Return 1
    test.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    test.get(2)  # Returns -1 (not found)
    test.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    test.get(1)  # Return -1 (not found)
    test.get(3)  # Return 3
    test.get(4)  # Return 4
    print(f'Runtime for our solution: {time() - sol_start}\n')
