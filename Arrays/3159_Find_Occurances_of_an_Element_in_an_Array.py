class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = [i for i in range(len(nums)) if nums[i] == x]
        i = 0
        q = len(queries)
        while i < q:
            if queries[i] <= len(indices):
                queries[i] = indices[queries[i]-1]
            else:
                queries[i] = -1
            i += 1
        return queries
                
        