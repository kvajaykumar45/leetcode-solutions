class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums)-1
        if high == 0 and target == nums[0]:
            return [0,0]
        elif high==0 and target != nums[0]:
            return [-1,-1]
            
        first = -1
        last = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                for i in range(mid, -1, -1):
                    if nums[i] != target:
                        first = i+1
                        break
                else:
                    first=0
                for i in range(mid, len(nums)):
                    if nums[i] != target:
                        last = i-1
                        break
                else:
                    last=len(nums)-1
                break
            elif nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1 
        return [first,last]
        
