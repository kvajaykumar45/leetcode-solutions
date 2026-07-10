class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(2*n - 1, -1, -1):
            num = nums[i % n]
            while stack and stack[-1] <= num:
                stack.pop()
            if i < n:
                ans[i] = stack[-1] if stack else -1
            stack.append(num)
        return ans
