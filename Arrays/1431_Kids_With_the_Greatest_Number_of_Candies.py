class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for each in candies:
            if (each + extraCandies) >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result

        
