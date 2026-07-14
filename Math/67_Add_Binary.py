class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1=0
        exp=0
        for i in range(len(a)-1,-1,-1):
            num1=num1 + (2**exp) * int(a[i])
            exp=exp+1
             
        num2=0
        exp=0
        for i in range(len(b)-1,-1,-1):
            num2=num2+(2**exp) * int(b[i])
            exp=exp+1
        num3=num1+num2
        return bin(num3)[2:]
       


   
       

        
