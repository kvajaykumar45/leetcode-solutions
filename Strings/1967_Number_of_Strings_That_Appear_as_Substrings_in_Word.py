class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for each in patterns:
            if each in word:
                count += 1
        return count
        
