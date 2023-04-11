#!/usr/bin/python3

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
            

obj = Solution()
nums = [0, 0, 0]
print(obj.threeSum(nums))