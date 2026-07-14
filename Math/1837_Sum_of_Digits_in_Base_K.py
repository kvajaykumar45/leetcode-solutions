class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result_sum=0
        while(n!=0):
            r=n%k
            result_sum=result_sum+r
            n=n//k
        return result_sum
