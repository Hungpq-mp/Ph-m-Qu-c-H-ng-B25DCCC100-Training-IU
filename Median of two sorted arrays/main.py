from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if not nums1 and not nums2:
            return 0.0
        num = nums1 + nums2
        num.sort()  
        nn = len(num)
        if nn == 0:
            return 0.0
        if nn % 2 != 0:    
            return float(num[nn // 2])
        else: 
            med = (num[nn // 2] + num[nn // 2 - 1]) / 2
            return med
sol = Solution()
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
print(sol.findMedianSortedArrays(nums1,nums2))