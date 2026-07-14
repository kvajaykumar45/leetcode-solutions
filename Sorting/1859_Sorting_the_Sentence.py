class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(each[:-1] for each in sorted(s.split(),key=lambda x:x[-1]))
        

        
