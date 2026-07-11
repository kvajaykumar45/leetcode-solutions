class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i=1
        mini = 10**6
        ans = []
        while i < len(arr):
            j = i - 1
            diff = abs(arr[i] - arr[j])
            if mini > diff:
                mini = diff
                ans = []
                ans.append([arr[j], arr[i]])
            elif mini == diff:
                ans.append([arr[j], arr[i]])
            i += 1
        return ans
