class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        k = []
        for each in s:
            if each == '*':
                k.pop()
            else:
                k.append(each)
        return "".join(k)
