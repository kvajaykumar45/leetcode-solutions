class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = len(arr)
        five = int(l*5/100)
        start = five - 0
        end = l-1-five
        return sum(arr[start:end+1])/(l-2*five)
        
