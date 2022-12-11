const { performance } = require('perf_hooks');

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution {
  mergeTwoSortedLists(list1, list2) {
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

  method(lists) {
    let previous = null;
    for (let i = 0; i < lists.length; i++) {
      previous = this.mergeTwoSortedLists(previous, lists[i]);
    }

    return previous;
  }

  reference(lists) {
    let previous = null;

    for (let i = 0; i < lists.length; i++) {
      previous = this.mergeTwoSortedLists(previous, lists[i]);
    }

    return previous;
  }

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.method(copy));
        else this.method(copy);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.reference(copy));
        else this.reference(copy);
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
    new ListNode(1, new ListNode(4, new ListNode(5))),
    new ListNode(1, new ListNode(3, new ListNode(4))),
    new ListNode(2, new ListNode(6)),
  ],
  [],
  [[]],
];
test.quantify(testCases);
