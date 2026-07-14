class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        p1 = nums[0:n]
        p2 = nums[n:]
        ans = []
        i = 0
        while i < n:
            ans.append(p1[i])
            ans.append(p2[i])
            i = i + 1

        return ans


        
