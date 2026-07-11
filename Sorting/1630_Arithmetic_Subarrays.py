class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for j in range(0,len(l)):
            x = nums[l[j] : r[j]+1 ]
            x.sort()
            k = x[1] - x[0]
            for i in range(2, len(x)):
                if x[i] - x[i-1] != k:
                    res.append(False)
                    break
            else:
                res.append(True)
        return res    


        
