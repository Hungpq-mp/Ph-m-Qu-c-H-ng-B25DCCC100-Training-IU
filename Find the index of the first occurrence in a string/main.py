class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       return haystack.find(needle) 
sol = Solution()
haystack = input()
needle = input()
print(sol.strStr(haystack,needle))