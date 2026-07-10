class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        applescount = sum(apple)
        i = 0
        count = 0
        while applescount > 0 and i < len(capacity):
            applescount = applescount - capacity[i]
            count = count + 1
            i += 1
        return count



        
