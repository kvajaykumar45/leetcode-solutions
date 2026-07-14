class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        def sum_multiples(k):
            m = n // k
            return k * m * (m + 1) // 2

        # This part uses the inner function
        total = (
            sum_multiples(3) +
            sum_multiples(5) +
            sum_multiples(7)
            - sum_multiples(15)
            - sum_multiples(21)
            - sum_multiples(35)
            + sum_multiples(105)
        )
        return total

        
