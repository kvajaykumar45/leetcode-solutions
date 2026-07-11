class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        encrypt=[]
        su=0
        for each in nums:
            large = 0
            count = 0
            while each != 0:
                r = each % 10
                if r > large:
                    large = r
                each = each // 10
                count += 1
            number=0
            for i in range(count):
                number = number*10 + large
            su = su + number
        return su
            


        
