class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        result = []

        for i in range(length):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % length]
            elif k < 0:
                for j in range(1, -k + 1):
                    total += code[(i - j + length) % length]
            else:
                total = 0
            result.append(total)

        return result
