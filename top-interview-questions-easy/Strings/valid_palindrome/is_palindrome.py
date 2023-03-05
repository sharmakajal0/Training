import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(s.maketrans('', '', string.punctuation))
        
        s = s.replace(' ', '')
        s = s.lower()

        str_temp = s[::-1]
        
        if s == str_temp:
            return True
        return False

s = input()
is_palindrome = Solution()
print(is_palindrome.isPalindrome(s))