class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for each in "abcdefghijklmnopqrstuvwxyz":
            last = word.rfind(each)
            first = word.find(each.upper())
            if last!= -1 and first!= -1:
                if last < first:
                    count += 1
        return count     