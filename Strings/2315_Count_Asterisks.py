class Solution:
    def countAsterisks(self, s: str) -> int:

        count = 0
        stars = 0
        for each in s:
            if each == '|':
                count += 1
            elif each == '*' and count % 2 == 0:
                stars += 1
        return stars
        
