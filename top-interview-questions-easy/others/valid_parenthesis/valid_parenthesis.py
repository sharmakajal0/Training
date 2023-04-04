#!/usr/bin/python3 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
            



obj = Solution()
s = "(([{}]))"
print(obj.isValid(s))