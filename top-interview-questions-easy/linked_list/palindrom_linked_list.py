from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head

        stack = []
        
        ret = True

        while slow != None:
            stack.append(slow.val)
            slow = slow.next
        
        while head:

            i = stack.pop()

            if head.val == i:
                ret = True
            else:
                ret = False
                break
            
            head = head.next
        
        return ret

head = ListNode()
solve = Solution()
solve.isPalindrome(head)