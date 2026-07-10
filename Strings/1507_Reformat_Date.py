class Solution:
    def reformatDate(self, date: str) -> str:
        parts = date.split()
        result = parts[2] + "-"
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        result = result + months[parts[1]] +"-"
        days = [str(i) for i in range(1,10)]
        day = parts[0][:-2]
        if day in days:
            day = "0"+day
            result += day
        else:
            result += day
        return result
        
        
