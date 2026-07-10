class Solution:
    def generateTag(self, caption: str) -> str:
        result = "#"
        words = caption.split()
        length = len(words)
        if length > 0:
            result += words[0].lower()
        for i in range(1,length):
            result += words[i].title()
        if len(result) > 100:
            return result[:100] 
        else:
             return result

        
