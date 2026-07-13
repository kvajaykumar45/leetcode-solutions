class Solution:
    def maxScore(self, s: str) -> int:
        mscore=0
        for i in range(0,len(s)-1):
            left=s[0:i+1]
            right=s[i+1:]
            score=0
            for k in left:
                if k == '0':
                    score+=1
            for h in right:
                if h == "1":
                    score+=1
            if score > mscore:
                mscore = score
        return mscore



