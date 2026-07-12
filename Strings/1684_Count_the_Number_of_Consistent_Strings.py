class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for each in words:
            flag = True
            for k in each:
                if k not in allowed:
                    flag = False
                    break
            if flag == True:
                c+=1
        return c

            
                

        
