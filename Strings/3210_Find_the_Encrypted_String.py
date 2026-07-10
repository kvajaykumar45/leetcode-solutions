class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        result = ""
        length = len(s)
        i = 0
        while i < length:
            result += s[ (i+k)%length ]
            i = i + 1
        return result
        
