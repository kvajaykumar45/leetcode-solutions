class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexed_score = [(s, i) for i, s in enumerate(score)]
        indexed_score.sort(reverse=True)
        result = [""] * len(score)
        for rank, (s, i) in enumerate(indexed_score):
            if rank == 0:
                result[i] = "Gold Medal"
            elif rank == 1:
                result[i] = "Silver Medal"
            elif rank == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank + 1)
        return result


        
