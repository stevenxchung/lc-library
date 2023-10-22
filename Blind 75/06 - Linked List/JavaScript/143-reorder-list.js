const { performance } = require("perf_hooks");

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution {
  method(head) {
    let [slow, fast] = [head, head.next];

    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
    }

    // Reverse p2
    let l2 = slow.next;
    let [prev, temp] = [null, null];
    slow.next = null;
    while (l2) {
      temp = l2.next;
      l2.next = prev;
      prev = l2;
      l2 = temp;
    }

    let l1 = head;
    let [temp1, temp2] = [null, null];
    l2 = prev;
    while (l2) {
      [temp1, temp2] = [l1.next, l2.next];
      l1.next = l2;
      l2.next = temp1;
      [l1, l2] = [temp1, temp2];
    }

    return head;
  }

  reference(head) {
    const mid = this.getMid(head); /* Time O(N) */
    const reveredFromMid = this.reverse(mid); /* Time O(N) */

    this.reorder(head, reveredFromMid); /* Time O(N) */

    return head;
  }

  getMid = (head) => {
    let [slow, fast] = [head, head];

    while (fast && fast.next) {
      /* Time O(N) */
      slow = slow.next;
      fast = fast.next.next;
    }

    return slow;
  };

  reverse = (head) => {
    let [prev, curr, next] = [null, head, null];

    while (curr) {
      /* Time O(N) */
      next = curr.next;
      curr.next = prev;

      prev = curr;
      curr = next;
    }

    return prev;
  };

  reorder = (l1, l2) => {
    let [first, next, second] = [l1, null, l2];

    while (second.next) {
      /* Time O(N) */
      next = first.next;
      first.next = second;
      first = next;

      next = second.next;
      second.next = first;
      second = next;
    }
  };

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
  new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4)))),
  new ListNode(
    1,
    new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))
  ),
];
test.quantify(testCases);
