/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?
*/

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
  queue = [];
  dict = {};
  limit = capacity;
};

/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
  // Check to see if key exists
  if (dict[key] === (null || undefined)) {
    return -1;
  }

  let lastValue = 0;
  // Put key to the end
  for (let i = 0; i < queue.length; i++) {
    if (queue[i] === key) {
      lastValue = queue.splice(i, 1);
      // Add element to front of queue
      queue.unshift(lastValue);
    }
  }

  return dict[key];
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
  // Check if limit has been reached
  if (queue.length == limit) {
    delete dict[queue.pop()];
  }
  queue.unshift(key);
  dict[key] = value;
};

cache = new LRUCache(2 /* capacity */);

console.log(
  cache.get(2),
  cache.put(2, 6),
  cache.get(1),
  cache.put(1, 5),
  cache.put(1, 2),
  cache.get(1),
  cache.get(2)
);

// obj = {
//   test: 1
// };

// let testFunc = obj => {
//   if (obj['test']) {
//     console.log("Yo it's true!");
//   } else {
//     console.log("Yo it's false!");
//   }
//   console.log('object value:', obj['test']);
// };

// testFunc(obj);
