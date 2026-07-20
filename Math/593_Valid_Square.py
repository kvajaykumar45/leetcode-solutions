class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        sides = [p1, p2, p3, p4]
        sq = []
        for i in range(len(sides)):
            for j in range(i+1, len(sides)):
                k = self.squaredist(sides[i], sides[j])
                sq.append(k)
                
        sq.sort()
        return ( sq[0] > 0 and
    sq[0] == sq[1] == sq[2] == sq[3] and
    sq[4] == sq[5] )

    def squaredist(self, x, y):
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
