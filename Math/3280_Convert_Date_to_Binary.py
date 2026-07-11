class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y,m,d=map(int,date.split('-'))
        s = bin(y)[2:] + '-' + bin(m)[2:] + '-' + bin(d)[2:]
        return s
