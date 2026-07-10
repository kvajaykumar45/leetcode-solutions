class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for each in words:
            s=""
            for i in each:
                if i != separator:
                    s = s + i
                else:
                    if s != "":
                        result.append(s)
                        s=""
            else:
                if s != "": result.append(s)
        return result
"""
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            for part in word.split(separator):
                if part:
                    result.append(part)
        return result
"""
