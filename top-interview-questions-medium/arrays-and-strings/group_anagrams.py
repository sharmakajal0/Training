#!/usr/bin/python3

from typing import List, DefaultDict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())

        


obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(obj.groupAnagrams(strs))