class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self. heap = nums
        self. klarge = k
        heapq.heapify(self.heap)
        while len(self. heap) > self.klarge:
            heapq.heappop(self.heap)
        #print(self.heap, self.klarge)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.klarge:
            heapq.heappop(self.heap)
            
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
