class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x % 10 ==0 and  x != 0:
            return False
        n = 0
        while x > n:
            n = (n *10) + x%10
            x = x// 10
        return (x == n) or (x == n //10)
