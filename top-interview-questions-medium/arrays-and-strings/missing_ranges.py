#!/usr/bin/python3

from typing import List

class Solution:
    def missingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []

        for i in nums:
            if i == lower:
                pass
        
        if lower == upper:
            return [str(lower)]
        else:
            return [f"{lower}->{upper}"]






obj = Solution()
nums = list(map(int, input().split()))
print(obj.missingRanges(nums))