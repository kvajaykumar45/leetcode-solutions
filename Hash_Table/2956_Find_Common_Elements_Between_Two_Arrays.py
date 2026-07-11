class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        answer = [0,0]
        for each in nums1:
            if each in s2:
                answer[0] += 1
        
        for each in nums2:
            if each in s1:
                answer[1] += 1
        return answer
