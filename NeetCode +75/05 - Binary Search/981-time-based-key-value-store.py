'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns ''.
'''

from time import time


class TimeMap:
    def __init__(self, debug=False):
        # Consists of key: [(timestamp_i, value_i)...]
        self.map = {}
        self.debug = debug

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = self.map.get(key, [(timestamp, value)])
        else:
            self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, arr = '', self.map.get(key, [])
        # Binary search to find timestamp if exists
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][0] <= timestamp:
                res = arr[m][-1]
                # Close on to the latest timestamp
                l = m + 1
            else:
                r = m - 1

        if self.debug:
            print(f'get({key, timestamp}): {res}')
        return res


if __name__ == '__main__':
    test = TimeMap(debug=True)
    sol_start = time()
    # Store the key 'foo' and value 'bar' along with timestamp = 1.
    test.set('foo', 'bar', 1)
    # Return 'bar'
    test.get('foo', 1)
    # Return 'bar', since there is no value corresponding to 'foo' at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is 'bar'.
    test.get('foo', 3)
    # Store the key 'foo' and value 'bar2' along with timestamp = 4.
    test.set('foo', 'bar2', 4)
    # Return 'bar2'
    test.get('foo', 4)
    # Return 'bar2'
    test.get('foo', 5)

    print('\nAdditional testing...')
    test.set('foo', 'bar3', 7)
    test.get('yeet', 5)  # Return ""
    test.get('foo', 1)  # Return 'bar'
    test.get('foo', 2)  # Return 'bar'
    test.get('foo', 3)  # Return 'bar'
    test.get('foo', 4)  # Return 'bar2'
    test.get('foo', 5)  # Return 'bar2'
    test.get('foo', 6)  # Return 'bar2'
    test.get('foo', 7)  # Return 'bar3'
    test.get('foo', 8)  # Return 'bar3'
    print(f'Runtime for our solution: {time() - sol_start}\n')
