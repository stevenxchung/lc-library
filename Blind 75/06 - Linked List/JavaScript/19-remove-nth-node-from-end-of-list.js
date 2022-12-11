const { performance } = require('perf_hooks');

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution {
  method(head, n) {
    let node = new ListNode();
    node.next = head;
    let [p1, p2] = [node, head];
    for (let i = 0; i < n; i++) {
      p2 = p2.next;
    }
    while (p2) {
      p1 = p1.next;
      p2 = p2.next;
    }
    p1.next = p1.next.next;

    return node.next;
  }

  reference(head, n) {
    const length = this.getNthFromEnd(head, n); /* Time O(N) */

    const isHead = length < 0;
    if (isHead) return head.next;

    const curr = this.moveNode(head, length); /* Time O(N) */

    curr.next = curr.next.next;

    return head;
  }

  getNthFromEnd = (curr, n, length = 0) => {
    while (curr) {
      /* Time O(N) */
      curr = curr.next;
      length++;
    }

    return length - n - 1;
  };

  moveNode = (curr, length) => {
    while (length) {
      /* Time O(N) */
      curr = curr.next;
      length--;
    }

    return curr;
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input[0]));
        if (i === 0) console.log(this.method(copy, input[1]));
        else this.method(copy, input[1]);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input[0]));
        if (i === 0) console.log(this.reference(copy, input[1]));
        else this.reference(copy, input[1]);
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
    new ListNode(
      1,
      new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))
    ),
    2,
  ],
  [new ListNode(1), 1],
  [new ListNode(1, new ListNode(2)), 1],
];
test.quantify(testCases);
