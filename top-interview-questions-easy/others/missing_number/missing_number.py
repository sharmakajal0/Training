from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        num_sum = sum(nums)
        actual_sum = (n * (n + 1)) // 2
        
        return actual_sum - num_sum


obj = Solution()
nums = [1, 0, 3, 4]
print(obj.missingNumber(nums))