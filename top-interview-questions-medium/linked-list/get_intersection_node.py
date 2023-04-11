#!/usr/bin/python3

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


    # def printList(self, head: ListNode):
    #     while head is not None:
    #         print(head.val, end=" ")
    #         head = head.next

headA = ListNode(4)
for i in range(4):
    value = ListNode(int(input()))
    headA.next = value
    if i == 3:
        headA.next == None
    else:
        headA = headA.next

headB = ListNode(5)
for i in range(5):
    value = ListNode(int(input()))
    headB.next = value
    if i == 4:
        headB.next == None
    else:
        headB = headB.next

obj = Solution()
getHead = obj.getIntersectionNode(headA, headB)
obj.printList(getHead)