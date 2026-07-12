class Solution:
    def frequencySort(self, s: str) -> str:
        f={}
        for each in s:
            if each in f:
                f[each] += 1
            else:
                f[each] = 1
        k = sorted(f.items(), key=lambda x: x[1], reverse=True)
        result=""
        for each,c in k:
            result += each*c
        return result



        
