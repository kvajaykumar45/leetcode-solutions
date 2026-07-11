class Solution:
    def maximum69Number (self, num: int) -> int:
        k = str(num)
        for i in range(len(k)):
            if k[i] == '6':
                k=k[:i]+'9'+k[(i+1):]
                break
        return int(k)
        
