from collections import Counter
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        freq=Counter(nums)
        unique_vals=list(freq.values())
        result=0
        left=0
        total=sum(unique_vals)
        for count in unique_vals:
            total-=count
            result+=left*total*count
            left+=count
        return result
