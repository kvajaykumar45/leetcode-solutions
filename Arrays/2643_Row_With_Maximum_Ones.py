class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        maxindex=0
        maxcount=0
        for i, row in enumerate(mat):
            c=0
            for val in row:
                if val == 1:
                    c+=1
            if c > maxcount:
                maxcount = c
                maxindex = i
           
        return [maxindex, maxcount]

        
