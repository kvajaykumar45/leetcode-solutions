class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount=0
        count=0
        for each in nums:
            if each == 1:
                count+=1
            else:
                if count > maxcount:
                    maxcount = count
                count=0
        if count > maxcount:
            maxcount=count
        return maxcount
