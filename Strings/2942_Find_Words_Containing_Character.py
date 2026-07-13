class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        target=[]
        for i in range(0,len(words)):
            if x in words[i]:
                target.append(i)
        return target
        
