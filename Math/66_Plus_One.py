class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in digits:
            num=num*10+i
        num=num+1
        List=[]
        while(num!=0):
            r=num%10
            List.insert(0,r)
            num=num//10
        return List
        
