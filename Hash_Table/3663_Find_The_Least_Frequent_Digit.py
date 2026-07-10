class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        d = {}
        while n > 0:
            r = n % 10
            if r in d:
                d[r] += 1
            else:
                d[r] = 1
            n = n // 10
        #print(d)

        minvalue = min(d.values())
        keys = [k for k,v in d.items() if v == minvalue]
        return min(keys)
