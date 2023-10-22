const { performance } = require("perf_hooks");

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution {
  method(head) {
    let [prev, node] = [null, head];

    while (node) {
      const temp = node.next;
      node.next = prev;
      prev = node;
      node = temp;
    }

    return prev;
  }

  reference(head) {
    let [prev, curr, next] = [null, head, null];

    while (curr) {
      /* Time O(N) */
      next = curr.next;
      curr.next = prev;

      prev = curr;
      curr = next;
    }

    return prev;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        // Create deep copy
        input = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.method(input));
        else this.method(input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        // Create deep copy
        input = JSON.parse(JSON.stringify(input));
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
const testCases = [
  new ListNode(
    1,
    new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))
  ),
  new ListNode(1, new ListNode(2)),
  null,
];
test.quantify(testCases);
