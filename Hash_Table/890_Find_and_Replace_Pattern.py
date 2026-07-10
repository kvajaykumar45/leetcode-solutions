class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for each in words:
            x = self.replace(each, pattern)
            if x:
                ans.append(each)
        return ans

    def replace(self, word, pattern):
        d1 = {}
        d2 = {}
        n = len(word)
        m = len(pattern)
        if n!= m:
            return False
        for i in range(n):
            if word[i] not in d1:
                d1[word[i]] = pattern[i]
            else:
                if d1[word[i]] != pattern[i]:
                    return False
            
            if pattern[i] not in d2:
                d2[pattern[i]] = word[i]
            else:
                if d2[pattern[i]] != word[i]:
                    return False
            
        return True

        
