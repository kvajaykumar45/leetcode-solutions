class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        astart=[int(x) for x in arriveAlice.split('-')]
        bstart=[int(x) for x in arriveBob.split('-')]
        aleave=[int(x) for x in leaveAlice.split('-')]
        bleave=[int(x) for x in leaveBob.split('-')]

        astartdays=astart[1]
        month=1
        for i in range(1,astart[0]):
            astartdays+=days[i]

        bstartdays=bstart[1]
        for i in range(1,bstart[0]):
            bstartdays+=days[i]

        aleavedays=aleave[1]
        month=1
        for i in range(1,aleave[0]):
            aleavedays+=days[i]
        
        bleavedays=bleave[1]
        month=1
        for i in range(1,bleave[0]):
            bleavedays+=days[i]
        
        commstart=max(astartdays,bstartdays)
        commleave=min(aleavedays,bleavedays)

        return max(0,commleave-commstart+1)


        
