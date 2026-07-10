class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        answer = []

        for i in range(left, right+1):
            for each in ranges:
                #print(each)
                if i >= each[0] and i <= each[1]:
                    answer.append(True)
                    break
                
            else:
                answer.append(False)
        #print(answer)
        return all(answer)

        
