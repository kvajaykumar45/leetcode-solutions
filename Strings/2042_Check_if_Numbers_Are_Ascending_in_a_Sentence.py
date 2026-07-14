class Solution:
    def areNumbersAscending(self, s: str) -> bool:
            '''
            k=s.split()
            nums=[]
            for i in k:
                if i.isdigit():
                    nums.append(int(i))
            '''
            nums= [int(i) for i in s.split() if i.isdigit()]
            for i in range(0,len(nums)-1):
                if nums[i] >= nums[i+1]:
                    return False
            return True
        
        
