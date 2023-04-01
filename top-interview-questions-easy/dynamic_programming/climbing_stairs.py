class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        one_step, two_step = 1, 2
        all = 0

        for i in range(2, n):
            all = one_step + two_step
            one_step = two_step
            two_step = all
        
        return all

stairs = Solution()
print(stairs.climbStairs(int(input())))