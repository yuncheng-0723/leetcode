class Solution:
    def isPalindrome(self, x: int) -> bool:    
        reverseX = str(x)[::-1]
        return True if str(x) == reverseX else False
        