class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        '''
        if n == 1:
            return max(quantities)
        '''
        low = 1
        high = max(quantities)
        while low <= high:
            mid = (low + high)//2
            shops = 0
            for each in quantities:
                shops += (each + mid - 1) // mid
            if shops <= n:
                high = mid-1
            else:
                low = mid+1
        return low
        
