class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        equal=[]
        big=[]

        for each in nums:
            if each < pivot:
                small.append(each)
            elif each == pivot:
                equal.append(each)
            else:
                big.append(each)
        nums = small + equal + big
        return nums
        
