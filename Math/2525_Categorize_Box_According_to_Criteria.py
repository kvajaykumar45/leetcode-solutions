class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        bulky = (length >= 10**4 or width >= 10**4 or height >= 10**4) or (length * width * height) >= 10**9
        heavy = mass >= 100

        if (bulky and heavy):
            return "Both"
        elif (not bulky and not heavy):
            return "Neither"
        elif (bulky and not heavy):
            return "Bulky"
        elif (heavy and not bulky):
            return "Heavy"
       
