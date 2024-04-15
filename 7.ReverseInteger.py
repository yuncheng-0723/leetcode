class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        reverseX = "-" + strX[1:][::-1] if ("-" in str(x)) else strX[::-1]
        if (int(reverseX) < (-2**31)) or (int(reverseX) > (2**31)-1):
            return 0
        return int(reverseX)