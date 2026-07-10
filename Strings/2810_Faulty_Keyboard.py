class Solution:
    def finalString(self, s: str) -> str:
        result=[]
        for i in s:
            if i != 'i':
                result.append(i)
            else:
                result.reverse()
        return ''.join(result)
        
