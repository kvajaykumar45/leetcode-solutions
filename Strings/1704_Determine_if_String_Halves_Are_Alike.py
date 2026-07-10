class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        x = 0
        n = len(s)//2
        lcount = rcount = 0
        for i in range(n):
            if s[i] in vowels:
                lcount+=1
        for i in range(n,len(s)):
            if s[i] in vowels:
                rcount += 1
        return lcount == rcount
        
