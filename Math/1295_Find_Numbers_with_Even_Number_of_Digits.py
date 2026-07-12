import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for each in nums:
            digits = int(math.log10(each)) + 1
            if digits % 2 == 0:
                count += 1
        return count
        
