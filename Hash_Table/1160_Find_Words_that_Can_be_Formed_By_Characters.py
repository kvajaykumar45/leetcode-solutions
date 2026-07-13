class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= chars_count.get(c, 0) for c in word_count):
                total += len(word)

        return total
        
