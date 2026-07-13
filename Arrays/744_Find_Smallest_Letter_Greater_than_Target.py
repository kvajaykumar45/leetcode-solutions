class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        for i in range(0,len(letters)):
            if target < letters[i]:
                return letters[i]
        return letters[0]
        
        
