class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numset = set()
        duplicate = 0

        for i in range(n):
            if nums[i] in numset:
                duplicate = nums[i]
            else:
                numset.add(nums[i])
        print(numset, duplicate)

        for i in range(1,n+1):
            if i not in numset:
                missing = i
                break
        return [duplicate, missing]
