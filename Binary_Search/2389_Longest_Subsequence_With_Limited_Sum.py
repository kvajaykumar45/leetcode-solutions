class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        answer = []
        prefixsum = [0] * len(nums)
        prefixsum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixsum[i] = prefixsum[i-1] + nums[i]
        #print(prefixsum)
        for target in queries:
            low = 0
            high = len(prefixsum) - 1
            while low <= high:
                mid = (low + high) // 2
                if prefixsum[mid] <= target: 
                    low = mid + 1
                else:
                    high = mid - 1
            answer.append(low)
        return answer

