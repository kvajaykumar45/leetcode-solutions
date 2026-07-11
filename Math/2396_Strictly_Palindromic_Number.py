class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for i in range(2, n-1):
            print(i)
            
            s = ""
            m = n
            while m != 0:
                r = m%i
                s = s + str(r)
                m = m//i
            #print(s,i)
            if s != s[::-1]:
                return False
        return True

            
        
