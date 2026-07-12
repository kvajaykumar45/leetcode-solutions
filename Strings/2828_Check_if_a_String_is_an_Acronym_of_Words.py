"""
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym = ''.join(word[0] for word in words)
        return acronym == s
"""

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acr=""
        for each in words:
            acr += each[0]
        return acr == s
        
