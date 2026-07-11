class Solution:
    def totalMoney(self, n: int) -> int:
        prevmonday = 0
        bank = 0
        while n != 0:
            monday = prevmonday + 1
            prevmonday = monday
            amt = monday
            count = 1
            while count<=7 and n>0:
                bank = bank + amt
                amt += 1
                count += 1
                n = n - 1
        return bank
        
