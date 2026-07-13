class Solution:
    def toLowerCase(self, s: str) -> str:
        s1 = ""
        for i in s:
            if ord(i) in range(65,91):
                s1+=chr(ord(i)+32)
            else:
                s1+=i
        return s1
        
