class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a1=a
        b1=b
        count = 0
        while b1!=0:
            a1, b1 = b1, a1%b1

            
        for i in range(1, a1+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count
