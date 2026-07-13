class Solution:
    def replaceDigits(self, s: str) -> str:
        result=""
        length=len(s)
        i=0
        while i<length-1:
            
            x=chr(ord(s[i]) + int(s[i+1]))
            result = result+s[i]+x
            i=i+2
        if i==length-1:
            result+=s[i]
        return result
        
