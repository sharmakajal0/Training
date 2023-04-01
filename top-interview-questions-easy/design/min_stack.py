#!/usr/bin/python3

from typing import List

class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self) -> int:
        if len(self.stack) > 0:
            return min(self.stack)
        return None 
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(12)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)