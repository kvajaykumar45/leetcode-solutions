class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [0,1]
        first = fib[0]
        second = fib[1]
        third = first + second
        while third <= k:
            fib.append(third)
            first = second
            second = third
            third = first + second
        #print(fib)
        ans = 0
        i = len(fib) - 1
        while (i >= 0):
            if fib[i] <= k:
                ans += 1
                k = k - fib[i]
                if k == 0:
                    break
            i = i - 1
        return ans
            

            
            
        
        
