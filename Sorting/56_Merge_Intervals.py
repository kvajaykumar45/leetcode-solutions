class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged = []
        for each in intervals:
            if not merged:
                merged.append(each)
            elif each[0] > merged[-1][1]:
                merged.append(each)
            else:
                merged[-1][1] = max(merged[-1][1], each[1])
        return merged

        
