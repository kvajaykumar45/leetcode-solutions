class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        vowels = [0] * 26
        cons = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            if ch in vowels_set:
                vowels[idx] += 1
            else:
                cons[idx] += 1

        vmax = max(vowels) if any(vowels) else 0
        cmax = max(cons) if any(cons) else 0

        return vmax + cmax
