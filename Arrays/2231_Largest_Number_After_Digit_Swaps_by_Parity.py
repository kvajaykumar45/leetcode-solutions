class Solution:
    def largestInteger(self, num: int) -> int:
        number = [int(i) for i in str(num)]
        
        even = []
        odd = []
        for i in number:
            if i % 2 == 0:
                even.append(i)
            elif i % 2 == 1:
                odd.append(i)

        even = sorted(even, reverse=True)
        odd = sorted(odd, reverse=True)

        eIndex = 0
        oIndex = 0
        for i in range(len(number)):
            if number[i] % 2 == 0:
                number[i]  = even[eIndex]
                eIndex = eIndex + 1
            
            elif number[i] % 2 == 1:
                number[i] = odd[oIndex]
                oIndex = oIndex + 1

        n = ""
        for i in number:
            n  = n  + str(i)

        return int(n)     
