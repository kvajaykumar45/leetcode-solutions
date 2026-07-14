class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n * (n + 1) // 2  
        left_sum = 0
        for x in range(1, n + 1):
            left_sum += x
            right_sum = total - (x * (x - 1)) // 2
            if left_sum == right_sum:
                return x
        return -1
        

        
