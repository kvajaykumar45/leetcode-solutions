class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        for i in s.split():
            words.append(i[::-1])
        return ' '.join(words)
    
        
