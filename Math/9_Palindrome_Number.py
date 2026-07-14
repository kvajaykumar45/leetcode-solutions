class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        k=str(x)[::-1]
        if k==str(x):
            return True
        else:
            return False
        

       
