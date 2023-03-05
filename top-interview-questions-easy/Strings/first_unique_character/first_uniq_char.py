
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chr = ""
        for i in s:
            count = s.count(i)
            if count == 1:
                chr = i
                break
        
        if chr != '':
            return s.index(chr)
        return -1
            
        

s = input()
unique = Solution()
print(unique.firstUniqChar(s))