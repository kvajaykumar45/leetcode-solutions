class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = {}
        d2 = {}
        words = s.split()
        n = len(pattern)
        m = len(words)
        if m!=n:
            return False
        for i in range(n):
            if pattern[i] not in d1:
                d1[pattern[i]] = words[i]
            else:
                if d1[pattern[i]] != words[i]:
                    return False
            if words[i] not in d2:
                d2[words[i]] = pattern[i]
            else:
                if d2[words[i]] != pattern[i]:
                    return False

        return True

    
        
