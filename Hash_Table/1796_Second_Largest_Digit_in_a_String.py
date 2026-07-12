class Solution:
    def secondHighest(self, s: str) -> int:
        nums=set()
        for i in s:
            if i.isdigit():
                nums.add(int(i))
        if len(nums) < 2:
            return -1
        return sorted(nums)[-2]
        
        
