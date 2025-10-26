class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        return nums1.sort()
sol = Solution()
nums1 = list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(sol.merge(nums1,nums2))