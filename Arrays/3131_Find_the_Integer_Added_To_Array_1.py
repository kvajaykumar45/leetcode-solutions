class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums2.sort()
        return min(nums2) - min(nums1)
        
