from typing import List

class Solution:
    def rotate(self, nums: List[int], d: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = d % len(nums)
        print(d)
        self.reverseArray(nums, 0, len(nums) - 1)
        self.reverseArray(nums, 0, d - 1)
        self.reverseArray(nums, d, len(nums) - 1)
    
    def reverseArray(self, arr: List[int], d: int, n: int) -> None:
        first = d
        last = n

        while (first < last):
            temp = arr[first]
            arr[first] = arr[last]
            arr[last] = temp
            first += 1
            last -= 1




nums = list(map(int, input().split(" ")))
d = int(input())
rotation = Solution()
rotation.rotate(nums, d)
print(nums)
