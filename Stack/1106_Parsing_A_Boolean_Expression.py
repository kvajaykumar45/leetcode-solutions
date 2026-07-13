class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == 't':
                stack.append(True)
            elif c == 'f':
                stack.append(False)
            elif c in ['!', '&', '|', '(']:
                stack.append(c)
            elif c == ')':
                items = []
                while stack[-1] != '(':
                    items.append(stack.pop())
                stack.pop()
                op = stack.pop()
                if op == '!':
                    stack.append(not items[0])
                elif op == '&':
                    stack.append(all(items))
                elif op == '|':
                    stack.append(any(items))
                elif op == ',':
                    continue
        return stack[0]
