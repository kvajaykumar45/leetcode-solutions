class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        turns=min(x,y//4)
        if turns%2 == 0:
            return "Bob"
        else:
            return "Alice"
        
