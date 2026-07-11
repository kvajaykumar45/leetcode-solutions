class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        i = 0
        while i < len(command) - 1:
            if command[i] == 'G':
                s += command[i]
                i += 1
            elif command[i] == '(' and command[i+1] == 'a':
                s += command[i+1]
                i += 2
            elif command[i] == 'l' and command[i+1] == ')':
                s += command [i]
                i += 2
            elif command[i] == '(' and command[i+1] == ')':
                s += 'o'
                i += 2
        
        if i == len(command)-1 and command[i] == 'G':
            s += 'G'
        
        return s
        
