class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        divsum=1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divsum = divsum + i
                if i != num//i:
                    divsum = divsum + num//i
        if divsum == num:
            return True
        else:
            return False
        
