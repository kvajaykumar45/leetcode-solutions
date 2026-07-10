class Solution:
    def heapify(self, heap, n, i):
        smallest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and heap[left][0] < heap[smallest][0]:
            smallest = left
        if right < n and heap[right][0] < heap[smallest][0]:
            smallest = right

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(heap, n, smallest)
    
    def buildMinHeap(self, heap):
        n = len(heap)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(heap, n, i)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for each in nums:
            if each not in d:
                d[each] = 1
            else:
                d[each] += 1

        heap = []
        for num, freq in d.items():
            heap.append((freq,num))
            self.buildMinHeap(heap)

            if len(heap) > k:
                heap[0],heap[-1] = heap[-1],heap[0]
                heap.pop()
                self.heapify(heap, len(heap), 0)
        x = []
        for each in heap:
            x.append(each[1])
        return x

        
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(dict(Counter(nums).most_common(k)))
"""
