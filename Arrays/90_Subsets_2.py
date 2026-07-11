class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        for num in nums:
            x = [curr + [num] for curr in result]
            #print(x)
            for k in x:
                if k not in result:
                    result.append(k)
        return result

        
    

        
