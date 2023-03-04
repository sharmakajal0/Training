from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            sum = target - num
            if sum not in h:
                h[num] = i
            else:
                return [h[sum], i]

# nums = [2, 6, 7, 5, 43, 21, 3, 5, 17, 27]
nums = list(map(int, input("Enter the list of integers with a space: ").split(" ")))
target = int(input("Enter the Target: "))
# target = 44
two_sum = Solution()
print(two_sum.twoSum(nums, target))
