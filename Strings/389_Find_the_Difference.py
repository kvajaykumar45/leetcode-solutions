class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for each in s:
            t=t.replace(each,'',1)
        return t        
            
            
                
        
        
