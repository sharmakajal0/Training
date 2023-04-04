#!/usr/bin/python3

from typing import List

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: 
            return 0
        composites = [False] * n
        limit = int(n ** 0.5)
        for i in range(2, limit + 1):
            if composites[i] == False:
                for j in range(i * i, n, i):
                    composites[j] = True
        
        count = 0
        for i in range(2, n):
            if composites[i] == False:
                count += 1
        
        return count

obj = Solution()
print(obj.countPrimes(10))