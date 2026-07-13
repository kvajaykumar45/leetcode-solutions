class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for each in s:
            if each.isdigit():
                stk.pop()
            else:    
                stk.append(each)
        return ''.join(stk)
        
