from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        for fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast +=1
            else:
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1
        
        return slow + 1



nums = [1,1,2]
sol = Solution()
print(sol.removeDuplicates(nums))
