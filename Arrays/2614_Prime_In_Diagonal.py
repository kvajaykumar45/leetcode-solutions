class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        diagonals=[]
        i=0
        while i < len(nums):
            k=nums[i][i]
            if self.isPrime(k):
                diagonals.append(k)
            i=i+1
        
        c=len(nums)-1
        r=0
        while r < len(nums):
            if r != c:
                k=nums[r][c]
                if self.isPrime(k):
                    diagonals.append(k)
            r = r + 1
            c = c - 1
        if len(diagonals) == 0:
            return 0
        else:
            return max(diagonals)
        
        


    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
