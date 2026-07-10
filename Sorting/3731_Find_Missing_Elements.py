class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        i = nums[0]
        n = nums[-1]
        while i <= n:
            if i not in nums:
                result.append(i)
            i = i + 1
        return result
        

        
