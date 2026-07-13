class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i.lower() in word and i.upper() in word:
                count += 1
        return count

        
