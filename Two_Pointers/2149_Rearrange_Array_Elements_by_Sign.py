class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        combine = []
        for i in nums:
            if i > 0:
                positives.append(i)
            else:
                negatives.append(i)
        for i in range(len(positives)):
            combine.append(positives[i])
            combine.append(negatives[i])
        return combine

        
