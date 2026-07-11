class Solution:
    def dayOfYear(self, date: str) -> int:
        days=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        year, month, day = map(int, date.split('-'))
        dayC = 0
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0) and month>2:
            dayC=1
        dayC =  dayC + days[month-1] + day
        return dayC
        
