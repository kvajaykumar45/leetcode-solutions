class Solution:
    def minOperations(self, logs: List[str]) -> int:

        ops = []

        for each in logs:
            if each == "../"  and ops != []:
                ops.pop()
            elif each == '../' and ops == []:
                continue
            elif each == "./":
                continue
            else:
                ops.append(each)
            #print(ops)
        return len(ops)
        
