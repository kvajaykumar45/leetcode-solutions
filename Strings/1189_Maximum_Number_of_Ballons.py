class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        d = {}
        for ch in text:
            if ch in "balloon":
                d[ch] = d.get(ch,0) + 1
        return min(
            d.get('b', 0),
            d.get('a', 0),
            d.get('l', 0) // 2,
            d.get('o', 0) // 2,
            d.get('n', 0)
        )
