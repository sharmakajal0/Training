from typing import List

class Solution:
    def intersectionOfThreeArrays(self, n1: int, n2: int, n3: int, arr1: List, arr2: List, arr3: List) -> List:
        x_loc, y_loc, z_loc = 0, 0, 0
        res = []

        while x_loc != n1 and y_loc != n2 and z_loc != n3:
            x, y, z = arr1[x_loc], arr2[y_loc], arr3[z_loc]
            
            if x == y and y == z:
                res.append(x)
                x_loc, y_loc, z_loc = x_loc + 1, y_loc + 1, z_loc + 1
            elif x <= y and x <= z:
                x_loc += 1
            elif y <= x and y <= z:
                y_loc += 1
            else:
                z_loc += 1
        
        return res

n1 = int(input())
n2 = int(input())
n3 = int(input())
arr1 = list(map(int, input().split(" ")))[:n1]
arr2 = list(map(int, input().split(" ")))[:n2]
arr3 = list(map(int, input().split(" ")))[:n3]
solve = Solution()
print(solve.intersectionOfThreeArrays(n1, n2, n3, arr1, arr2, arr3))
