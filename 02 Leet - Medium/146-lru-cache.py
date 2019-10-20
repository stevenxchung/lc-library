'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?
'''


# class DLNode:
#     def __init__(self):
#         self.key = 0
#         self.value = 0
#         self.next = None
#         self.prev = None


# class LRUCache:
#     def __init__(self, capacity):
#         self.cache = {}
#         self.size = 0
#         self.capacity = capacity
#         self.head, self.tail = DLNode(), DLNode()

#         self.head.next, self.tail.prev = self.tail, self.head

#     # Always adds to the front of cache
#     def add_node(self, node):
#         node.prev, node.next = self.head, self.head.next
#         self.head.next.prev, self.head.next = node, node

#     # Remove node in constant time no matter where in the linked list
#     def remove_node(self, node):
#         prev, new = node.prev, node.next
#         prev.next, new.prev = new, prev

#     # Simply becomes remove from list and add back (recall that adding a node always puts the node back to the front of the cache)
#     def to_front(self, node):
#         self.remove_node(node)
#         self.add_node(node)

#     # Remove last node (least recently used)
#     def remove_last(self):
#         last = self.tail.prev
#         self.remove_node(last)
#         return last

#     def get(self, key):
#         node = self.cache.get(key)
#         # If node does not exist
#         if not node:
#             return -1
#         self.to_front(node)

#         return node.value

#     def put(self, key, value):
#         node = self.cache.get(key)
#         #  If node does not exist, add to list
#         if not node:
#             newNode = DLNode()
#             newNode.key = key
#             newNode.value = value

#             self.cache[key] = newNode
#             self.add_node(newNode)

#             self.size += 1

#             # If capacity has been reached, remove the last node
#             if self.size > self.capacity:
#                 last = self.remove_last()
#                 del self.cache[last.key]
#                 self.size -= 1
#         # Otherwise, node exists and should be updated and moved to the front of the list
#         else:
#             node.value = value
#             self.to_front(node)

class DNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity=0):
        # Will be a stack
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DNode(), DNode()

        self.head.next, self.tail.prev = self.tail, self.head


# Test
cache = LRUCache()
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4
