from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        
        while count < len(nums):
            nums[count] = 0
            count += 1


nums = list(map(int, input().split(" ")))
move_zeroes = Solution()
move_zeroes.moveZeroes(nums)
print(nums)