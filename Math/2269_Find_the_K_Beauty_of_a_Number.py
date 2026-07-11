class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        copy = num
        digits = []
        while copy != 0:
            digits.insert(0, copy%10)
            copy = copy // 10
        print(digits)
        kbeauty = 0
        for i in range(0, len(digits)-k+1):
            number = 0
            for j in range(i, i+k):
                number = number * 10 + digits[j]
            print(number)
            if number !=0 and num % number == 0:
                kbeauty += 1
        return kbeauty


        
