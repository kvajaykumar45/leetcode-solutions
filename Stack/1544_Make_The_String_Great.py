class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if stk and abs(ord(s[i]) - ord(stk[-1])) == 32:
                stk.pop()
            else:
                stk.append(s[i])
        return "".join(stk)
"""
class Solution:
    def makeGood(self, s: str) -> str:
        
        stk = []
        stk.append(s[0])
        for i in range(1, len(s)):
            if stk and s[i] == stk[-1]:
                stk.append(s[i])
            elif stk and s[i].lower() == stk[-1].lower():
                stk.pop()
            else:
                stk.append(s[i])
        return "".join(stk)

"""
