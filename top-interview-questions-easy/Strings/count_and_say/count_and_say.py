class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.count(self.countAndSay(n - 1))
    
    def count(self, s):
        c = s[0]
        count = 1
        res = ""
        for char in s[1:]:
            if char == c:
                count += 1
            else:
                res = res + str(count) + c
                c = char
                count = 1
        res = res + str(count) + c
        return res

n = 3
count_and_say = Solution()
print(count_and_say.countAndSay(n))
