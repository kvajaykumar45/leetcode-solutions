class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        finish = []
        f = set(friends)
        for i in order:
            if i in f:
                finish.append(i)
        return finish

        
