class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        k=bin(n)[2:][::-1]
        print(k)
        even=0
        odd=0
        i=0
        while i < len(k):
            if k[i] == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
            i += 1
        return [even, odd]
        
