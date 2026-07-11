class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        #print(count)
        ans = []
        for each in nums:
            if count[each] > len(nums)//3 and each not in ans:
                ans.append(each)
        return ans
