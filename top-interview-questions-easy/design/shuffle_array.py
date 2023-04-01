#!/usr/bin/python3

from typing import List
import random

class Solution:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = self.nums[:]
        for i in range(len(shuffled) - 1, 0, -1):
            j = random.randrange(0, i + 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled


nums = [1, 2, 3, 4]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
