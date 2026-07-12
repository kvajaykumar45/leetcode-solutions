class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        for each in jewels:
            c+=stones.count(each)
        return c
