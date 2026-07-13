class Solution:
    def greatestLetter(self, s: str) -> str:

        k=list()
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if i in s and i.lower() in s:
                k.append(i)
        if len(k) != 0:
            return max(k)
        else:
            return ""
        
