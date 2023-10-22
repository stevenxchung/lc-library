const { performance } = require("perf_hooks");

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution {
  method(list1, list2) {
    let res = new ListNode();
    let temp = res;
    while (list1 && list2) {
      if (list1.val <= list2.val) {
        temp.next = list1;
        list1 = list1.next;
      } else {
        temp.next = list2;
        list2 = list2.next;
      }
      temp = temp.next;
    }

    temp.next = list1 || list2;

    return res.next;
  }

  reference(list1, list2) {
    let sentinel = new ListNode();
    let tail = sentinel;

    while (list1 && list2) {
      /* Time O(N + M) */
      const islist2Greater = list1.val <= list2.val;
      const islist2Less = list2.val < list1.val;

      if (islist2Greater) {
        tail.next = list1;
        list1 = list1.next;
      }

      if (islist2Less) {
        tail.next = list2;
        list2 = list2.next;
      }

      tail = tail.next;
    }

    tail.next = list1 || list2;

    return sentinel.next;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        // Create deep copy
        const input1 = JSON.parse(JSON.stringify(input[0]));
        const input2 = JSON.parse(JSON.stringify(input[1]));
        if (i === 0) console.log(this.method(input1, input2));
        else this.method(input1, input2);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        // Create deep copy
        const input1 = JSON.parse(JSON.stringify(input[0]));
        const input2 = JSON.parse(JSON.stringify(input[1]));
        if (i === 0) console.log(this.reference(input1, input2));
        else this.reference(input1, input2);
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
    new ListNode(1, new ListNode(2, new ListNode(4))),
    new ListNode(1, new ListNode(3, new ListNode(4))),
  ],
  [null, null],
  [null, new ListNode(0)],
];
test.quantify(testCases);
