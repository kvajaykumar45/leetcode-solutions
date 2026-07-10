class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0 for i in range(n)]
        odds = 0
        evens = 0
        for i in range(n-1, -1, -1):
            if nums[i] % 2 == 0:
                answer[i] = odds
                evens += 1
            else:
                answer[i] = evens
                odds += 1
        return answer
           
        
