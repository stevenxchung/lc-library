const { performance } = require("perf_hooks");

class Solution {
  method(numCourses, prerequisites) {
    let adjList = Array.from({ length: numCourses }, () => []);
    for (const [a, b] of prerequisites) {
      adjList[a].push(b);
    }

    let seen = new Set();

    const dfs = (course) => {
      if (seen.has(course)) return false;
      if (adjList[course].length === 0) return true;

      seen.add(course);
      for (const prereq of adjList[course]) {
        if (!dfs(prereq)) return false;
      }
      seen.delete(course);
      adjList[course] = [];

      return true;
    };

    for (const [course, prereq] of adjList.entries()) {
      if (!dfs(course)) return false;
    }

    return true;
  }

  reference(numCourses, prerequisites) {
    const graph = this.createGraph(numCourses, prerequisites);
    let seen = new Set();
    let seeing = new Set();

    const explore = (course) => {
      if (seen.has(course)) return true;
      if (seeing.has(course)) return false;

      seeing.add(course);
      for (let neighbor of graph[course]) {
        if (!explore(neighbor)) return false;
      }

      seen.add(course);
      seeing.delete(course);
      return true;
    };

    for (let i = 0; i < numCourses; i++) {
      if (!explore(i)) return false;
    }

    return true;
  }

  createGraph(numCourses, edges) {
    const graph = Array.from({ length: numCourses }, () => []);

    for (let edge of edges) {
      let [a, b] = edge;

      if (!(a in graph)) graph[a] = [];
      if (!(b in graph)) graph[b] = [];

      graph[a].push(b);
    }

    return graph;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(...input));
        else this.method(...input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
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
  [2, [[1, 0]]],
  [
    2,
    [
      [1, 0],
      [0, 1],
    ],
  ],
  // Additional
  [
    5,
    [
      [0, 1],
      [0, 2],
      [1, 3],
      [1, 4],
      [3, 4],
    ],
  ],
  [
    3,
    [
      [0, 1],
      [1, 2],
      [2, 0],
    ],
  ],
];
test.quantify(testCases);
