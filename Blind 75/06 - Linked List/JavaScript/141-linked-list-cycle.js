const { performance } = require("perf_hooks");

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution {
  method(head) {
    let [p1, p2] = [head, head];
    while (p1 && p2 && p2.next) {
      if (p1.val == p2.val) return true;
      p1 = p1.next;
      p2 = p2.next.next;
    }
    return false;
  }

  reference(head) {}

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
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
let t1 = new ListNode(3, new ListNode(2, new ListNode(0)));
const temp = new ListNode(-4, t1.next);
t1.next.next.next = temp;

let t2 = new ListNode(1, new ListNode(2));
t2.next.next = t2;
const testCases = [t1, t2, new ListNode(1)];
test.quantify(testCases);
