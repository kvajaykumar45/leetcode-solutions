class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = list()
        for each in range(left, right+1):
            value = each
            while each > 0:
                rem = each % 10
                if rem ==0 or value % rem != 0:
                    break
                each //= 10
            else:
                result.append(value)
        return result
        
