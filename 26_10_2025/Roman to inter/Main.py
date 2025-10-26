class Solution:
    def romanToInt(self, s: str) -> int:
        lst = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        tong = 0
        n = len(s)
        for i in range(n):
            cur = lst[s[i]]
            if i + 1 < n and lst[s[i+1]] > cur:
                tong -= cur
            else:
                tong += cur
                
        return tong

sol = Solution()
s = input()
print(sol.romanToInt(s))