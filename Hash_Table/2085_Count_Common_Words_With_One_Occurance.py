class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        count = 0
        
        for word in c1.keys() & c2.keys():
            if c1[word] == 1 and c2[word] == 1:
                count += 1
        return count


        
