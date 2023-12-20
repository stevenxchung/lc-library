'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         temp = ListNode(0)
#         temp.next = l1
#         print(temp.next)
#         self.help(l1, l2, temp, 0)
#         print(temp.next)
#         return temp.next

#     def help(self, l1, l2, temp, carry):
#         if l1 and l2:
#             sum = l1.val + l2.val + carry
#             l1.val = sum % 10
#             self.help(l1.next, l2.next, temp.next, sum//10)
#         elif l1:
#             sum = l1.val + carry
#             l1.val = sum % 10
#             self.help(l1.next, None, temp.next, sum//10)
#         elif l2:
#             sum = l2.val + carry
#             l2.val = sum % 10
#             temp.next = l2  # If l2 is truthy then set temp.next to l2
#             self.help(None, l2.next, temp.next, sum//10)
#         else:
#             if carry:
#                 temp.next = ListNode(carry)


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = n = ListNode(0)
        # While and of the below are true
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            print(carry, val)
            n.next = n = ListNode(val)
        return result.next
