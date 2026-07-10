"""
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(each) for each in matrix]
"""        

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        degrees = []
        for each in matrix:
            degrees. append(sum(each))
        return degrees
        
