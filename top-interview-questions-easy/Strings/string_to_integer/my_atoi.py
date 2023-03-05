class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s_list = s.split(' ')
        return_string = ''
        for i in s_list:
            if i != '':
                for j in range(1, len(i)):
                    if i[j].isnumeric():
                        return_string += i[j]
        return_value = int(return_string)
        if return_value > (-1) * (2 ** 31) and return_value < (2 ** 31) - 1:
            return return_value
        else:
            return 0



s = input()
my_atoi = Solution()
print(my_atoi.myAtoi(s))