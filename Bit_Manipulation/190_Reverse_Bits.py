class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n,'032b')
        return int(bits[::-1], 2)
        
