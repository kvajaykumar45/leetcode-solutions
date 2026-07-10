class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        result = {}
        for each in items1:
            result[each[0]] = each[1]
        
        for each in items2:
            if each[0] in result:
                result[each[0]] += each[1]
            else:
                result[each[0]] = each[1]
        my_list = [[k, result[k]] for k in sorted(result)]
        return my_list
        
