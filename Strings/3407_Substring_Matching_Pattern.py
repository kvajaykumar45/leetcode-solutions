class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        w = p.find("*")
        index1 = -1
        index2 = -1
        index1 = s.find(p[:w])
        if index1 == -1:
            return False
        index2 = s.find(p[w+1:], index1 + len(p[:w]))
        if index2 == -1:
            return False
        return True
        
        
