class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        s = 0 
        if k > numOnes:
            s = s + numOnes
            k = k - numOnes
        elif k  == numOnes:
            s = s + numOnes
            return s
        else:
            s = s + k
            return s
        print(s)
        if k > numZeros:
            k = k - numZeros
        elif k == numZeros:
            return s
        else:
            return s
        print(s)
        if k > numNegOnes:
            s = s - numNegOnes
            k = k - numNegOnes
        elif k == numNegOnes:
            s = s - numNegOnes
            return s
        else:
            s = s - k
            print(s)
            return s
        print(s)
        return s 

        
        
