class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum=0
        doubleSum=0
        for i in nums:
            if i < 10:
                singleSum += i
            else:
                doubleSum += i
        if singleSum == doubleSum:
            return False
        return True
        
