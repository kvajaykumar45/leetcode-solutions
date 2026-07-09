class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        previous = ''.join(sorted(words[0]))
        for each in words[1:]:
            current = ''.join(sorted(each))
            if previous != current:
                result.append(each)
                previous = current
        return result