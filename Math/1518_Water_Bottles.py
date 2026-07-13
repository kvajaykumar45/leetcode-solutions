class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink=numBottles
        while not numBottles<numExchange:
            exchange=numBottles//numExchange
            numBottles=exchange + (numBottles % numExchange)
            #print(numBottles)
            drink+=exchange
        return drink



        
