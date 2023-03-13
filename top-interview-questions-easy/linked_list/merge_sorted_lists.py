from typing import Optional

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    

class solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = new_list = ListNode()

        ptr1 = list1
        ptr2 = list2

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                current.next = ptr1
                ptr1, current = ptr1.next, ptr1
            else:
                current.next = ptr2
                ptr2, current = ptr2.next, ptr2
        
        if ptr1 or ptr2:
            current.next = ptr1 if ptr1 else ptr2
        
        return new_list.next
    
    def printList(self, head: Optional[ListNode]):
        while head:
            if head.next != None:
                print(head.val, end="->")
                head = head.next
            else:
                print(head.val)
                head = head.next    

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = None
list1 = node1
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6
node6.next = None
list2 = node4
solve = solution()
head = solve.mergeTwoLists(list1, list2)
solve.printList(head)
