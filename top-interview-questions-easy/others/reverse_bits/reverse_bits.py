

class Solution:
    def reverseBits(self, n: int) -> int:
        sum = 0

        for i in range(32):
            bit = (n >> i) & 1
            sum = sum | (bit << (31 - i))
        
        return sum

obj = Solution()
n = int(input())
print(obj.reverseBits(n))
