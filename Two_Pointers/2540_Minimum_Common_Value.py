class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        flag = False
        li=len(nums1)
        lj=len(nums2)
        while i < li and j < lj:
            if nums1[i] == nums2[j]:
                flag = True
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        if not flag:
            return -1
        
        
