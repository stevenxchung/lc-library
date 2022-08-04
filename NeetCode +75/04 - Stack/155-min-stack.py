'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
'''
from math import inf


class MinStack:
    def __init__(self, debug=False):
        self.debug = debug
        self.minimum = inf
        # Consists of a tuple (val, last minimum)
        self.min_stack = []

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.min_stack.append((val, self.minimum))

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        top = self.min_stack[-1][0]
        if self.debug:
            print(top)
        return top

    def getMin(self) -> int:
        min = self.min_stack[-1][1]
        if self.debug:
            print(min)
        return min


if __name__ == '__main__':
    test = MinStack(debug=True)
    test.push(-2)
    test.push(0)
    test.push(-3)
    test.getMin()  # return -3
    test.pop()
    test.top()    # return 0
    test.getMin()  # return -2
