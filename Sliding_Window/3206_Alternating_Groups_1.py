class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        
        n = len(colors)
        count = 0
        i=0
        while i < n:
            color = colors[i]
            prev = colors[i-1]
            next = colors[i+1] if i+1 < n else colors[0]
            if color != prev and color != next:
                count += 1
            i += 1
        
        return count
        
        

        
