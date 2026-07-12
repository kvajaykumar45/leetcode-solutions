class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable = []
        i = 1
        while i < len(height):
            if height[i-1] > threshold:
                stable.append(i)
            i += 1
        return stable


        
