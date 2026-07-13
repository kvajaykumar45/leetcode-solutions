class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i in range(0,len(s)):
            result +=  (123-ord(s[i]))* (i+1)
        return result


        
        
