class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        length = len(stones)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        while length != 1:
            stones.sort()
            max1=stones.pop()
            max2=stones.pop()
            diff=max1-max2
            stones.append(diff)
            length -= 1
        return stones[0]
