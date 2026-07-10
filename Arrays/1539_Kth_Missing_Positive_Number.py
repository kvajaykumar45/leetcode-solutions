class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        index = 0
        while True:
            if index < len(arr) and arr[index] == i:
                index = index + 1
            else:
                k = k - 1
                if k == 0:
                    break
            i = i + 1
        return i
        



        
