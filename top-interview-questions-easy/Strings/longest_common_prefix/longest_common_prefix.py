from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = zip(*strs)
        res = ''
        for i in a:
            if len(set(i)) == 1:
                res = res + i[0]

        return res


strs = ['flower', 'flow', 'flight']
common_prefix = Solution()
print(common_prefix.longestCommonPrefix(strs))