class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        for each in s:
            if each == '#' and s1 != []:
                s1.pop()
            elif each != '#':
                s1.append(each)
        
        s2 = []
        for each in t:
            if each == '#' and s2 != []:
                s2.pop()
            elif each != '#':
                s2.append(each)
        
        return s1 == s2
