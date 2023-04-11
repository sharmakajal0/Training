#!/usr/bin/python3

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


obj = Solution()
nums=[1,2,3,4,5]
print(obj.increasingTriplet(nums))