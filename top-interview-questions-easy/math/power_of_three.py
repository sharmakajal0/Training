#!/usr/bin/python3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            if n % 3 != 0:
                return False
            n = n // 3
        return n == 1


obj = Solution()
n = 27
print(obj.isPowerOfThree(n))
