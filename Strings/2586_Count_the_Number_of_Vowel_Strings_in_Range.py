class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count=0
        vowels=['a','e','i','o','u']
        for each in words[left:right+1]:
            if each[0] in vowels and each[-1] in vowels:
                count += 1
        return count
        
