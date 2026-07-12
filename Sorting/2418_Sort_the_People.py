"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [j for i, j in sorted(zip(heights, names), reverse=True)]
"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        i=0
        while i < len(heights):
            j = 0
            while j < len(heights)-1:
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1],heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                j+=1
            i+=1
        return names
