class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        print(nums)
        while nums != []:
            mini = nums.pop(0)
            maxi = nums.pop(-1)
            x=(mini + maxi)/2
            s.add(x)
        return len(s)

        
