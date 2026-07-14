class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        element = -1
        d = {}
        for i in nums:
            if i%2 == 0:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] = d[i] + 1 
        if not d:
            return -1
        max_val = max(d.values())
        max_keys = [k for k, v in d.items() if v == max_val]
        return min(max_keys)
