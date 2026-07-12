class Solution:
    def similarPairs(self, words: List[str]) -> int:
        each = 0
        pairs = 0
        while each < len(words) - 1:
            check = each + 1
            while check < len(words):
                if sorted(set(words[each])) == sorted(set(words[check])):
                        pairs += 1
                check += 1
            each += 1
        return pairs
        
