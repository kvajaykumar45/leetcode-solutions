class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for x in nums:
            each = int(x)
            heapq.heappush(heap, each)
            #print(heap)
            if len(heap) > k:
                heapq.heappop(heap)
        return str(heap[0])
