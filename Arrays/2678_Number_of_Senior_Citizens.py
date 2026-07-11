class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for each in details:
            x = int(each[11:13])
            
            if x > 60:
                count += 1
        return count
        
