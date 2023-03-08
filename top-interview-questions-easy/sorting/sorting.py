from typing import List

class Solution:
    def selectionSort(self, nums: List) -> None:
        n = len(nums)
        for i in range(n - 1):
            j = i + 1
            while j < n:
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
                

    def insertionSort(self, nums: List) -> None:
        n = len(nums)
        for i in range(1, n):
            j = i
            while j > 0:
                k = j - 1
                if nums[k] > nums[j]:
                    nums[k], nums[j] = nums[j], nums[k]
                j -= 1

    def bubbleSort(self, nums: List) -> None:
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    def mergeSort(self, nums: List) -> None:
        pass

nums = [3, 2, 1, 5, 4]
sorting = Solution()
sorting.mergeSort(nums)
print(nums)