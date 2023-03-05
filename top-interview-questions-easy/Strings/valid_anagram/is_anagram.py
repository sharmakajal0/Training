
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}
        for i in s:
            if i in h1:
                h1[i] += 1
            else:
                h1[i] = 1

        for i in t:
            if i in h2:
                h2[i] += 1
            else:
                h2[i] = 1

        if h1 == h2:
            return True
        return False

s = input()
t = input()
is_anagram = Solution()
print(is_anagram.isAnagram(s, t))
