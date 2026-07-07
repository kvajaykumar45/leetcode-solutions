class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        open=0
        for i in s:
            if i in ['[','(','{']:
                open=open + 1
        close=len(s)-open
        if open != close:
            return False
        stk=[]
        flag=True
        for i in s:
            if i=='(':
                stk.append(i)
            elif i=='[':
                stk.append(i)
            elif i=='{':
                stk.append(i)
            elif i==')':
                if len(stk) != 0 and stk.pop() != '(':
                    flag = False
                    break
            elif i==']':
                if len(stk) !=0 and stk.pop() != '[':
                    flag = False
                    break
            elif i=='}':
                if len(stk) != 0 and stk.pop() != '{':
                    flag = False
                    break
        
        if len(stk) != 0:
            flag=False

        return flag
