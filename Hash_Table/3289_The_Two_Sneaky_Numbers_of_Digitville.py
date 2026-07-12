from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        items=[]
        for each in nums:
            if each not in items:
                items.append(each)
            else:
                result.append(each)
        return result

"""
from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        f = Counter(nums)
        k = [each for each,c in f.items() if c == 2]
        return k
"""
