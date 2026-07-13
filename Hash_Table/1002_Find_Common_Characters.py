from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common_count = Counter(words[0])
        for word in words[1:]:
            common_count &= Counter(word)
        result = list(common_count.elements())
        return result

        
