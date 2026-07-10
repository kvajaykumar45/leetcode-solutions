class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            ans.append(i)
        for i in nums[::-1]:
            ans.append(i)

        return ans
        
