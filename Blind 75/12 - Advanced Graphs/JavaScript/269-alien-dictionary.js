const { performance } = require('perf_hooks');

class Solution {
  method(words) {
    let alienDict = {};
    for (const w of words) {
      for (const c of w) {
        alienDict[c] = new Set();
      }
    }
    for (let i = 0; i < words.length - 1; i++) {
      const [w1, w2] = [words[i], words[i + 1]];
      const minLength = Math.min(w1.length, w2.length);
      if (
        w1.length > w2.length &&
        w1.slice(0, minLength) === w2.slice(0, minLength)
      )
        return '';
      for (let j = 0; j < minLength; j++) {
        if (w1[j] !== w2[j]) {
          alienDict[w1[j]].add(w2[j]);
          break;
        }
      }
    }

    let seen = new Map();
    let res = [];

    const dfs = (c) => {
      if (seen.has(c)) return seen[c];

      seen.set(c, true);
      for (const neighbor of alienDict[c]) {
        if (dfs(neighbor)) return true;
      }
      seen.set(c, false);
      res.push(c);
    };

    for (const c of Object.keys(alienDict)) {
      if (dfs(c)) return '';
    }

    res.reverse();
    return res.join('');
  }

  reference(words) {
    const { graph, seen, buffer } = this.buildGraph(words);

    if (!this.canBuildGraph(words, graph)) return '';

    for (const [char] of graph) {
      if (!this.dfs(char, graph, seen, buffer)) return '';
    }

    return buffer.reverse().join('');
  }

  initGraph = () => ({
    graph: new Map(),
    seen: new Map(),
    buffer: [],
  });

  buildGraph = (words) => {
    const { graph, seen, buffer } = this.initGraph();

    for (const word of words) {
      for (const char of word) {
        graph.set(char, []);
      }
    }

    return { graph, seen, buffer };
  };

  canBuildGraph = (words, graph) => {
    for (let index = 0; index < words.length - 1; index++) {
      const [word1, word2] = [words[index], words[index + 1]];
      const minLength = Math.min(word1.length, word2.length);

      const isWord1Longer = word2.length < word1.length;
      const isPrefix = isWord1Longer && word1.startsWith(word2);

      if (isPrefix) return false;

      for (let j = 0; j < minLength; j++) {
        const [char1, char2] = [word1[j], word2[j]];

        const isEqual = char1 === char2;
        if (isEqual) continue;

        graph.get(char1).push(char2);

        break;
      }
    }

    return true;
  };

  dfs = (char, graph, seen, buffer) => {
    if (seen.has(char)) return seen.get(char);

    if (!this.backTrack(char, graph, seen, buffer)) return false;

    buffer.push(char);

    return true;
  };

  backTrack = (char, graph, seen, buffer) => {
    seen.set(char, false);
    for (const neighbor of graph.get(char)) {
      if (!this.dfs(neighbor, graph, seen, buffer)) return false;
    }
    seen.set(char, true);

    return true;
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
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
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
const testCases = [['wrt', 'wrf', 'er', 'ett', 'rftt']];
test.quantify(testCases);
