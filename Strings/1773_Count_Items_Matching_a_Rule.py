class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            for each in items:
                if each[0] == ruleValue:
                    count += 1
        elif ruleKey == "color":
            for each in items:
                if each[1] == ruleValue:
                    count += 1
        else:
            for each in items:
                if each[2] == ruleValue:
                    count += 1
        return count

"""
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        d = {'type':0, 'color':1, 'name':2}
        index = d[ruleKey]
        for each in items:
            if each[index] == ruleValue:
                count += 1
        return count
"""
