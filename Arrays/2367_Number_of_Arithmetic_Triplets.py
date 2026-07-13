class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        numset=set(nums)
        for num in numset:
            if (num - diff) in numset and (num-2*diff) in numset:
                count += 1
        return count
