class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for  i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
sol = Solution()
nums = list(map(int,input().split()))
target = int(input())
print(sol.twoSum(nums,target))