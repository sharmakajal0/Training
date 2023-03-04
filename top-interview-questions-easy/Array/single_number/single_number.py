from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}

        for i in range(len(nums)):
            if nums[i] in num_dict:
                num_dict[nums[i]] += 1
            else:
                num_dict[nums[i]] = 1
        
        items = num_dict.items()

        for key, value in items:
            if value == 1:
                return key
        
        return 0

my_list = list(map(int, input().split(" ")))
sol_obj = Solution()
print(sol_obj.singleNumber(my_list))
