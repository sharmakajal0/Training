

class Solution:
    def hammingDistance(self, x: int, y: int):
        n = x ^ y
        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
            n = n >> 1

        return count


obj = Solution()
x = int(input())
y = int(input())
print(obj.hammingDistance(x, y))