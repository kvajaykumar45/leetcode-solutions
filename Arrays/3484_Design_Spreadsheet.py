class Spreadsheet:
    def __init__(self, rows: int):
        self.sheet = [[0]*26 for i in range(rows)]
    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.sheet[row][col] = value
    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.sheet[row][col] = 0
    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        left, right = formula.split('+')
        return self.getOperandValue(left) + self.getOperandValue(right)
    def getOperandValue(self, s):
        if s.isdigit():
            return int(s)
        col = ord(s[0]) - ord('A')
        row = int(s[1:]) - 1 
        return self.sheet[row][col]

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
