# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# AC code
# tranverse the list to solve the problem
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = head = ListNode(0)
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            head.next = ListNode((val2+val1+carry) % 10)
            head = head.next
            carry = (val1+val2+carry)//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            head.next = ListNode(carry)
        return prehead.next
