class Solution:
    def isValid(self, word: str) -> bool:
        cons="bcdfghjklmnpqrstvwxyz"
        mini = False
        non = 0
        con = 0

        if len(word) >= 3:
            mini = True
        
        digit = False
        vowel = 0
        
        for ch in word:
            if ch in "0123456789":
                digit = True
            elif ch in "aeiouAEIOU":
                vowel += 1
            elif ch in cons or ch in cons.upper():
                con += 1
            else:
                non += 1
        if non != 0:
            return False
        if mini and bool(vowel) and bool(con):
            return True
        else:
            return False
            
        
