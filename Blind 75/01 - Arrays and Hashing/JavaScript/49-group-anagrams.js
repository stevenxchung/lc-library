const { performance } = require('perf_hooks');

const CODES = {
  a: 0,
  b: 1,
  c: 2,
  d: 3,
  e: 4,
  f: 5,
  g: 6,
  h: 7,
  i: 8,
  j: 9,
  k: 10,
  l: 11,
  m: 12,
  n: 13,
  o: 14,
  p: 15,
  q: 16,
  r: 17,
  s: 18,
  t: 19,
  u: 20,
  v: 21,
  w: 22,
  x: 23,
  y: 24,
  z: 25,
};

class Solution {
  method(strs) {
    let anagrams = {};
    for (const w of strs) {
      let id = new Array(26).fill(0);
      for (const c of w) {
        id[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
      }
      id = id.join('');

      if (id in anagrams) {
        anagrams[id].push(w);
      } else {
        anagrams[id] = [w];
      }
    }

    return Object.values(anagrams);
  }

  reference(strs) {
    const map = Object.create(null);
    for (const word of strs) {
      const hash = this.hashWord(word);
      if (!(hash in map)) {
        map[hash] = [];
      }
      map[hash].push(word);
    }

    const groups = [];
    for (const key in map) {
      groups.push(map[key]);
    }
    return groups;
  }

  hashWord = (word) => {
    const hash = new Array(26).fill(0);
    for (const ch of word) {
      ++hash[CODES[ch]];
    }
    return hash.toString();
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(input));
        else this.method(input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(input));
        else this.reference(input);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}
const test = new Solution();
const testCases = [['eat', 'tea', 'tan', 'ate', 'nat', 'bat'], [''], ['a']];
test.quantify(testCases);
