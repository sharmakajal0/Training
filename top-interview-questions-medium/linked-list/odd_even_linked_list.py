#!/usr/bin/python3

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        odd = head
        even = head.next

        evenHead = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next        
            even = even.next
        
        odd.next = evenHead
        return head

    def printList(self, head: Optional[ListNode]):
        while head is not None:
            print(head.val, end='->')
            head = head.next


one = ListNode(1)
two = ListNode(2)
one.next = two
three = ListNode(3)
two.next = three
four = ListNode(4)
three.next = four
five = ListNode(5)
four.next = five
five.next = None

obj = Solution()
obj.printList(one)
obj.oddEvenLinkedList(one)
obj.printList(one)