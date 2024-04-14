class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        substrings = []
        subString = ""

        for subS in s:
            if len(subString) == 0:
                subString += subS
            else:
                if subS in subString:
                    substrings.append(subString)
                    subString = subString[subString.index(subS)+1:]+subS
                else:
                    subString += subS
        if len(subString) > 0:
            substrings.append(subString)
            
        for i in substrings:
            maxCount = len(i) if len(i) > maxCount else maxCount

        return maxCount

        