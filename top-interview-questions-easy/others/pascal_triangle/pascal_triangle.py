from typing import List

class Solution:
    def pascalTriangle(self, n: int) -> List[List[int]]:
        res = [[1]]

        for i in range(n - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res

obj = Solution()
n = int(input())
print(obj.pascalTriangle(n))