class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        words = []
        if n < k:
            words.append(s + (fill * (k-n)))
            return words
        i=0
        start=0
        while i < n//k:
            start = i*k
            words.append(s[start:start+k])
            i += 1
        i = start + k
        left = n % k
        if left != 0:
            words.append(s[i:] + (fill * (k - left)))

        return words

        
