class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages=[]
        while nums != []:
            mini = nums.pop(0)
            maxi = nums.pop(-1)
            averages.append((mini+maxi)/2)
        return min(averages)
        
