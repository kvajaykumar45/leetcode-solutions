class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        m = len(nums2)
        n = len(nums1) - m
        nums3 = [0] *(n+m)
        k=0
        i=0
        j=0
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums3[k] = nums1[i]
                i += 1
                k += 1
            elif nums1[i] > nums2[j]:
                nums3[k] = nums2[j]
                j += 1
                k += 1
        
        while i < n:
            nums3[k] = nums1[i]
            k+=1
            i+=1
        
        while j < m:
            nums3[k] = nums2[j]
            j += 1
            k += 1
        
        for i in range(0, len(nums3)):
            nums1[i] = nums3[i]
