from math import log10

class Solution:
    def reverse(self, x: int) -> int:
        if x < -2147483648 or x > 2147483647:
            return 0
        res = 0
        sign = -1 if x < 0 else 1

        x = x * sign

        while x > 0:
            res = res * 10
            res += x % 10
            x = x // 10
        res = sign * res
        if res < -2147483648 or res > 2147483647:
            return 0
        else:
            return res

x = 1563847412

reverse_int = Solution()
print(reverse_int.reverse(x))