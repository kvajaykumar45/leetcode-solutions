class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        strings = 0
        for each in s:
            if each == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                strings += 1
        return strings
        