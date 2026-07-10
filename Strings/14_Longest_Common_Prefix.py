class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0
        common=""
        while i<len(strs[0]) and i<len(strs[-1]) and strs[0][i] == strs[-1][i]:
            common = common + strs[0][i]
            i = i + 1
        return common

        
