class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        
        if mainTank < 5:
            return mainTank * 10
        km = 0
        while mainTank >= 5 and additionalTank !=0:
            km = km + 50
            mainTank = mainTank - 5 + 1
            additionalTank -= 1
        return km + mainTank * 10 



        
            
        
