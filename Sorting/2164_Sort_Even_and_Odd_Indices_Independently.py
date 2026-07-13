class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens=nums[0::2]
        odds=nums[1::2]
        evens.sort()
        odds.sort(reverse=True)
        j=0
        k=0
        for i in range(0,len(nums)):
            if i%2==0:
                nums[i]=evens[j]
                j+=1
            else:
                nums[i]=odds[k]
                k+=1
        return nums
        
        
