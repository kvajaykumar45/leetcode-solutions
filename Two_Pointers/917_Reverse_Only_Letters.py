class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        right=len(s)-1
        result=list(s)
        while left<right:
            while left<right and not s[left].isalpha():
                left+=1
            while left<right and not s[right].isalpha():
                right-=1
            result[left],result[right] = result[right],result[left]
            left+=1
            right-=1
        return ''.join(result)
            


        
