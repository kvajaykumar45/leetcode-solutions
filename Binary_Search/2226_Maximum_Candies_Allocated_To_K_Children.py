class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        low = 1
        high = max(candies)
        total = sum(candies)
        if total < k:
            return 0
        while low <= high:
            mid = (low + high) // 2
            p = 0
            for each in candies:
                p += (each // mid)
            if p < k:
                high = mid - 1
            else:
                low = mid + 1
        return high

