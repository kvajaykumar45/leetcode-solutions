class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        k = list(s)
        v = []
        i = 0
        while i < len(s):
            if k[i] in vowels:
                v.append(k[i])
            i += 1
        v.sort()
        #print(v)
        i = 0
        j = 0
        while j < len(v):
            if k[i] in vowels:
                k[i] = v[j]
                i += 1
                j += 1
            else:
                i += 1
       # print(k)

        return ''.join(k)
