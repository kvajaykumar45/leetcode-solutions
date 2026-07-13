class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        # Flatten mat using list comprehension (faster than extend in a loop)
        flat = [num for row in mat for num in row]
        
        # Create the reshaped matrix using slicing in list comprehension
        return [flat[i:i+c] for i in range(0, len(flat), c)]

        
