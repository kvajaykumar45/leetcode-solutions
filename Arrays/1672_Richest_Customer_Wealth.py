class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth=0
        for i in accounts:
            temp=sum(i)
            if temp>wealth:
                wealth=temp
        return wealth

        
