class Solution:

    def heapify(self, nums, n, i):
        while True:
            parent = i
            leftchild = 2*i+1
            rightchild = 2*i+2

            if leftchild < n and nums[leftchild] > nums[parent]:
                parent = leftchild
        
            if rightchild < n and nums[rightchild] > nums[parent]:
                parent = rightchild
            if parent == i:
                return
            else:
                nums[parent], nums[i] = nums[i], nums[parent]
                i = parent
                
    
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n//2-1, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
        
        return nums 

        

        
