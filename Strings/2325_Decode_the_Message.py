class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        codes = {' ':' '}
        num = 97
        for each in key:
            if each != ' ' and each not in codes:
                codes[each] = chr(num)
                num += 1
        #print(codes)
        result = ""
        for i in message:
            result = result + codes[i]
        return result

        
