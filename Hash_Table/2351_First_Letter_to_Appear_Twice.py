class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s1 = set()
        for each in s:
            if each not in s1:
                s1.add(each)
            else:
                return each
        
        
