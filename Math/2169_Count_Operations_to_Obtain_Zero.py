class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                count+=num1//num2
                num1=num1%num2
            else:
                count+=num2//num1
                num2=num2%num1
            
        return count
       
