from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i in range(len(nums)):
            if nums[i] in duplicates:
                duplicates[nums[i]] += 1
            else:
                duplicates[nums[i]] = 1

        values = duplicates.values()
        for i in values:
            if i > 1:
                return True
        return False


nums = list(map(int, input().split(" ")))
obj_sol = Solution()
has_duplicates = obj_sol.containsDuplicate(nums)
if has_duplicates:
    print("true")
else:
    print("false")
