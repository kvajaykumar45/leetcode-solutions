class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        i=1
        count = 1 
        while i < len(chars):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count == 1:
                    s += chars[i-1]
                else:
                    s += chars[i-1]
                    s += str(count)
                    count = 1
            i += 1
        s += chars[-1]
        if count > 1:
            s+=str(count)
        
        
        print(s)
        chars[:]=list(s)
        
        return len(chars)

