class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n+1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        answer = []
        for each in queries:
            left = each[0]
            right = each[1]
            result = prefix[right+1] ^ prefix[left]
            answer.append(result)
        return answer

