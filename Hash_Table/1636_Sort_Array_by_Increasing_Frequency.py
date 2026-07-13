class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        f={}
        for i in nums:
            if i not in f:
                f[i] = 1
            else:
                f[i] += 1
        nums.sort(key=lambda x:(f[x],-x))
        return nums
        
