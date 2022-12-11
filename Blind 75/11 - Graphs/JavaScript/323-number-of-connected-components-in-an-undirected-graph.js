const { performance } = require('perf_hooks');

class Solution {
  method(n, edges) {
    let adjList = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
      adjList[a].push(b);
    }

    let seen = new Set();

    const dfs = (node) => {
      if (seen.has(node)) return false;
      seen.add(node);
      for (const n of adjList[node]) {
        dfs(n);
      }

      return true;
    };

    let count = 0;
    for (const [k, v] of adjList.entries()) {
      if (dfs(k)) count += 1;
    }

    return count;
  }

  reference(n, edges, count = 0) {
    const { graph, visited } = this.buildGraph(n, edges);

    for (const node in graph) {
      if (this.hasPath(graph, node, visited)) count++;
    }

    return count;
  }

  initGraph = (n) => ({
    graph: new Array(n).fill().map(() => []),
    visited: new Array(n).fill(false),
  });

  buildGraph = (n, edges) => {
    const { graph, visited } = this.initGraph(n);

    for (const [src, dst] of edges) {
      graph[src].push(dst);
      graph[dst].push(src);
    }

    return { graph, visited };
  };

  hasPath = (graph, current, visited) => {
    if (visited[current]) return false;
    visited[current] = current;

    for (const neighbor of graph[current]) {
      this.hasPath(graph, neighbor, visited);
    }

    return true;
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(...input));
        else this.method(...input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(...input));
        else this.reference(...input);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}

const test = new Solution();
const testCases = [
  [
    5,
    [
      [0, 1],
      [1, 2],
      [3, 4],
    ],
  ],
];
test.quantify(testCases);
