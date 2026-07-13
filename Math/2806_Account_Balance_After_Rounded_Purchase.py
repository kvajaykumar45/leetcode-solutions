class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        r=purchaseAmount%10
        q=purchaseAmount//10
         
        if purchaseAmount % 10 ==0:
            return 100-purchaseAmount
        elif r>=5:
            return 100-(q*10+10)
        elif r<5:
            return 100-(q*10)
        
