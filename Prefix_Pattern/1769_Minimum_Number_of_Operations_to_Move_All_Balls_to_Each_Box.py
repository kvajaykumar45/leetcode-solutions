class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0 for i in boxes]
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                #print('i=', i,'j=', j)
                
                if i != j and boxes[j] != '0':
                    answer[i] += abs(i-j)
        return answer

        
