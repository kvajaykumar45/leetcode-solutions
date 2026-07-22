class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        twenty = 0
        for each in bills:
            if each == 5:
                five += 5
            elif each == 10:
                if five >= 5:
                    five -= 5
                    ten += 10
                else:
                    return False
            elif each == 20:
                if five >= 5 and ten >= 10:
                    twenty += 20
                    five -= 5
                    ten -= 10
                elif five >= 15:
                    twenty += 20
                    five -= 15
                else:
                    return False
        return True
