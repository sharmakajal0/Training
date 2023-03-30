'''
Question: You are given an integer n and an array of size n - 1. The array contains all the numbers from 1 to n. Find the missing number.

Input:
    4
    4, 1, 2

Output:
    3
'''

from typing import List


class Solution:
    def missingNumber(self, n: int, arr: List) -> int:
        n_sum = (n * (n + 1))//2

        sum = 0

        for i in range(len(arr)):
            sum = sum + arr[i]

        missing = n_sum - sum

        return missing

n = int(input())
arr = list(map(int, input().split(" ")))[:n-1]
solve = Solution()
print(solve.missingNumber(n, arr))
