"""
class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        one = ord(c1[0]) + int(c1[1])
        two = ord(c2[0]) + int(c2[1])
        return one % 2 == two % 2
"""

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        if ord(coordinate1[0]) % 2 == 0 and int(coordinate1[1]) % 2 == 0:
            color1 = False
        elif ord(coordinate1[0]) % 2 == 1 and int(coordinate1[1]) % 2 == 1:
            color1 = False
        else:
            color1 = True

        if ord(coordinate2[0]) % 2 == 0 and int(coordinate2[1]) % 2 == 0:
            color2 = False
        elif ord(coordinate2[0]) % 2 == 1 and int(coordinate2[1]) % 2 == 1:
            color2 = False
        else:
            color2 = True
        
        return color1 == color2
