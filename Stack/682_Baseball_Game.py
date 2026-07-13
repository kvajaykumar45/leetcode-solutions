class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0
        for i in operations:
            if i == '+':
                newscore = record[-1] + record[-2]
                record.append(newscore)
                total += newscore
            elif i == 'D':
                newscore = 2 * record[-1]
                record.append(newscore)
                total += newscore
            elif i == 'C':
                total -= record.pop()
            else:
                record.append(int(i))
                total += int(i)
        return total
        
