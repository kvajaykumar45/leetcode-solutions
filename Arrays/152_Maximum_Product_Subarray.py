class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            a = cur_max * nums[i]
            b = cur_min * nums[i]
            temp_max = max(nums[i], a, b)
            cur_min = min(nums[i], a, b)
            cur_max = temp_max
            ans = max(cur_max, ans)
        return ans
        