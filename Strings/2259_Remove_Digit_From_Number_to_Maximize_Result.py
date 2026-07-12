class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        maxresult=0
        k=""
        i=0
        while i<len(number):
            if number[i] == digit:
                k = number[0:i] + number[(i+1): ]
                value = int(k)
                #print(value,type(value))
                if value > maxresult:
                    maxresult = value
            i += 1
        return str(maxresult)
            
