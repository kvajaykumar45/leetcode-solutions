class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = []
        altitude.append(0)
        for i in range(0,len(gain)):
            s = altitude[i] + gain[i]
            altitude.append(s)
        return max(altitude)

        
