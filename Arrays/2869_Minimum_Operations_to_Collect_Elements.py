class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mark = [0 for i in range(k+1)] 
        ops = 0
        count = 0
        i = len(nums) - 1
        while i >= 0:
            x = nums[i]
            if (x>=1 and x<=k) and mark[x] == 0:
                mark[x] = 1
                count += 1
            
            ops += 1
            #print(ops)
            if count == k:
                break
            i -= 1
        return ops 
            
