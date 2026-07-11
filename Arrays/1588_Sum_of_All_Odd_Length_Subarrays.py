class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for i in range(1, len(arr)+1, 2):
            for j in range(0, len(arr)-i+1):
                s += sum(arr[j:j+i])
        return s
