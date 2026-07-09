class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                diagonals[i-j].append(mat[i][j])
        for k in diagonals:
            diagonals[k].sort(reverse=True)
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = diagonals[i-j].pop()
        return mat
        
        