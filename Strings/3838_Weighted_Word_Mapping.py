class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        k="zyxwvutsrqponmlkjihgfedcba"
        t=0
        result=""
        for each in words:
            t=0
            for i in each:
                t += weights[ord(i) - 97]
            t = t%26
            result += k[t]
        return result
"""
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        s="abcdefghijklmnopqrstuvwxyz"
        index = {}
        rindex = {}
        for i in range(26):
            index[s[i]] = i
        k = s[::-1]
        for i in range(26):
            rindex[i] = k[i]
        s=0
        result=""
        for each in words:
            s=0
            for i in each:
                s += weights[index[i]]
            s = s%26
            result +=  rindex[s]
        return result
"""
