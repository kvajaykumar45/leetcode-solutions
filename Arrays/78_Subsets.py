class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        for num in nums:
            x = [curr + [num] for curr in result]
            result += x
        return result
    

        
