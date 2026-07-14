class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        r = []
        start,end = s.split(':')
        for i in range(ord(start[0]), ord(end[0])+1):
            for j in range(int(start[1]), int(end[1]) + 1 ):
                r.append(chr(i) + str(j))
        return r
