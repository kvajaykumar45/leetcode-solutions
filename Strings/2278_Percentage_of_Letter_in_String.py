class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = 0
        for each in s:
            if each == letter:
                c += 1
        return math.floor((c*100)/len(s))
        
