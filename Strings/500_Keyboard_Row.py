class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        result=[]
        for each in words:
            i=0
            while i<3:
                flag=True
                for k in each.lower():
                    if k not in rows[i]:
                        flag=False
                        break
                i+=1
                if flag:
                    result.append(each)
        return result

        
