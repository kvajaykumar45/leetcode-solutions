class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x < 0 :
            flag = True
            x = -x
        y=0
        while x > 0:
            r = x % 10
            y = y * 10 + r
            x = x // 10
        if flag:
            y = -y
        if -2**31 <= y <= 2**31:
            return y
        else:
            return 0
