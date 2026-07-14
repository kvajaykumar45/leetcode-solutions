class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        length=0
        for num in range(low,high+1):
            s=str(num)
            length=len(s)
            if length%2==0:
                p1=int(s[0:length//2])
                p2=int(s[length//2:])
                sum1=0
                while p1!=0:
                    r=p1%10
                    sum1=sum1+r
                    p1=p1//10
                sum2=0
                while p2!=0:
                    r=p2%10
                    sum2=sum2+r
                    p2=p2//10
                if sum1==sum2:
                    count+=1            
            else:
                continue
        return count




        
