class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        k=sentence.split()
        length=len(k)
        if length == 1:
            return sentence[0] == sentence[-1]
        i=0
        flag = True        
        while i < length:
            if k[i][-1] == k[(i+1)%length][0]:
                flag = True
            else:
                flag = False
                break
            i+=1
        return flag
            

        
        
