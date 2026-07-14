class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=0
        for i in s:
            x=ord(i)-96
            if x<10:
                n=n*10+x
            else:
                n=n*100+x

        for i in range(k):
            s=0
            while n>0:
                r=n%10
                s=s+r
                n=n/10
            n=s
        return n
        
        
