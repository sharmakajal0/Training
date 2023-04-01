#!/usr/bin/python3

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            next = i + rob1
            temp = max(next, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        

sol = Solution() 
nums = [2, 7, 9, 3, 1]
print(sol.rob(nums))
