    class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for each in tokens:
            if each not in '+-*/':
                stk.append(int(each))
            else:
                op2 = stk.pop()
                op1 = stk.pop()
                if each == '+':
                    stk.append(op1 + op2)
                elif each == '-':
                    stk.append(op1 - op2)
                elif each == '*':
                    stk.append(op1 * op2)
                elif each == '/':
                    stk.append(int(op1/op2))
        return stk[0]
        

        