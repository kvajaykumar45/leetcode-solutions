class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        answer = []
        row1 = []
        row2 = []
        for i in nums1:
            if i not in nums2 and i not in row1:
                row1.append(i)
        
        for i in nums2:
            if i not in nums1 and i not in row2:
                row2.append(i)
        answer.append(row1)
        answer.append(row2)

        return answer

"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        row1 = list(set1 - set2)
        row2 = list(set2 - set1)

        return [row1, row2]
"""
