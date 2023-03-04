from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1, pt2 = 0, 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break
        
        return res

nums1 = list(map(int, input().split(" ")))
nums2 = list(map(int, input().split(" ")))
intersection = Solution()
intersection_array = intersection.intersect(nums1, nums2)
print(intersection_array)

