class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        num=str(num)
        if num[len(num)-1] == '0':
            return False
        else:
            return True
