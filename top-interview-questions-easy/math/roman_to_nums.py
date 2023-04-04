class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        i = 0
        n = len(s)
        num = 0
        while i < n:
            try:
                if romans[s[i]] < romans[s[i + 1]]:
                    num += romans[s[i + 1]] - romans[s[i]]
                    i += 2
                    continue
                elif romans[s[i]] > romans[s[i + 1]]:
                    num += romans[s[i]]
                    i += 1
                else:
                    num += romans[s[i]]
                    i += 1
            except:
                num += romans[s[i]]
                i += 1

        return num

obj = Solution()

print(obj.romanToInt('IX'))
