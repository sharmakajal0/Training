from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s) - 1
        while first < last:
            temp = s[first]
            s[first] = s[last]
            s[last] = temp
            first += 1
            last -= 1


s = ["h","e","l","s","l","o","u"]
reverse_string = Solution()
reverse_string.reverseString(s)
print(s)