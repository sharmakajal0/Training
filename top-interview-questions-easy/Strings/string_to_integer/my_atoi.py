class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0


        s_list = list(s.strip())
        if len(s_list) == 0:
            return 0
        sign = -1 if s_list[0] == "-" else 1
        if s_list[0] in ['-', '+']:
            s_list.remove(s_list[0])
        ret= 0
        i = 0
        while i < len(s_list) and s_list[i].isdigit():
            ret = ret * 10 + ord(s_list[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2**31-1))



s = input()
my_atoi = Solution()
print(my_atoi.myAtoi(s))