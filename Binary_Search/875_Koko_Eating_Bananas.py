class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2
            hrs = 0
            for each in piles:
                hrs += (each + mid - 1) // mid
            if hrs <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
