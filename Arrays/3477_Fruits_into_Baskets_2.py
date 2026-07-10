class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        fill = [0] * n
        i = 0
        while i < n:
            j = 0
            while j < n :
                if fruits [i] <= baskets[j] and fill[j] == 0:
                    fill[j] = 1
                    break
                j += 1
            print(fill)
            i += 1
        
        return n - sum(fill)


        
