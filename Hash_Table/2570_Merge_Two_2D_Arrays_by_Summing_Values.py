class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = {}
        for each in nums1:
            result[each[0]] = each[1]
        
        for each in nums2:
            if each[0] in result:
                result[each[0]] += each[1]
            else:
                result[each[0]] = each[1]
        my_list = [[k, v] for k,v in result.items()]
        return sorted(my_list)
        
