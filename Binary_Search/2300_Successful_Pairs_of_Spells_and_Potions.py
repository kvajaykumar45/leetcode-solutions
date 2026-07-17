class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        pairs = []
        potions.sort()
        for i in spells:
            count = 0
            low = 0
            high = len(potions) - 1
            index = len(potions)
            while low <= high:
                mid = (low + high)//2
                if i * potions[mid] >= success:
                    index = mid
                    high = mid - 1
                else:
                    low = mid + 1
            pairs.append(len(potions) - index)
        return pairs



