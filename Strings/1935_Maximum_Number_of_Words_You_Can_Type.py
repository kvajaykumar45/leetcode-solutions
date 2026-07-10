class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0
        for each in words:
            status = True
            for i in each:
                if i in brokenLetters:
                    status = False
                    break
            if status == True:
                count += 1
        return count

        
