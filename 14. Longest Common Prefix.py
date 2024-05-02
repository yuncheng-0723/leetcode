class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        shortest_string = min(strs, key=len)

        for i in range(len(shortest_string)):
            isAllPrefixEqual = True
            for j in range(len(strs)):
                if(strs[j][i]!=shortest_string[i]): isAllPrefixEqual = False
            
            if(isAllPrefixEqual):
                common_prefix+=shortest_string[i]
            else:
                break

        return common_prefix
                

        