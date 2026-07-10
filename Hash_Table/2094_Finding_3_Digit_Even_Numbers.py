class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        supply = Counter(digits)
        answer = []

        for each in range(100, 1000,2):
            d1 = each // 100
            d2 = (each // 10) % 10
            d3 = each % 10
            demand = Counter([d1, d2, d3])
            if all(demand[i] <= supply[i] for i in demand):
                answer.append(each)
        return answer
