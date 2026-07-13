from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
        def f(d):
            year,month,day=[int(i) for i in d.split('-')]
            month_days = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]
            total_days = 0

            for y in range(1900, year):
                total_days += 366 if is_leap(y) else 365
            
            for m in range(1, month):
                if m == 2 and is_leap(year):
                    total_days += 29
                else:
                    total_days += month_days[m - 1]
            
            total_days += day - 1
            return total_days
        return abs(f(date1) - f(date2))



        
