class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        i = 0
        while i < len(nums):
            n = nums[i]
            while n > 0:
                r = n % 10
                if r==digit:
                    count += 1
                n = n // 10
            i += 1
        return count
''' 
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return str(nums).count(str(digit))
'''


