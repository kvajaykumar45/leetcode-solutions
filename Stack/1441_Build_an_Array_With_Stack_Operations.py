class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        i=1
        j=0
        while i < (n+1) and j < len(target):
            if i == target[j]:
                s.append("Push")
                j += 1
            else:
                s.append("Push")
                s.append("Pop")
            i += 1
            #print(s)
        return s
