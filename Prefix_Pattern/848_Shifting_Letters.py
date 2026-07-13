from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        shift_total = [0] * n
        shift_total[-1] = shifts[-1] % 26

        # Compute cumulative shifts in reverse
        for i in range(n - 2, -1, -1):
            shift_total[i] = (shifts[i] + shift_total[i + 1]) % 26

        # Apply shifts
        res = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + shift_total[i]) % 26 + ord('a'))
            res.append(new_char)

        return ''.join(res)
