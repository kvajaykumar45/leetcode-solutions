class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        def lower_bound(start, target):
            l, r = start, n
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        def upper_bound(start, target):
            l, r = start, n
            while l < r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m
            return l

        for i in range(n):
            l = lower_bound(i + 1, lower - nums[i])
            r = upper_bound(i + 1, upper - nums[i])
            count += r - l

        return count
