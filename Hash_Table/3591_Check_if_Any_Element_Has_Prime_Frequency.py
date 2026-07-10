class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        f = {}
        for each in nums:
            if each in f:
                f[each] += 1
            else:
                f[each] = 1
        print(f)
        primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67, 71,73,79,83,89,97}
        for each in f:
            if f[each] in primes:
                return True
        return False
        
