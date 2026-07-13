class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk=list()
        for c in s:
            if stk and stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)





        
