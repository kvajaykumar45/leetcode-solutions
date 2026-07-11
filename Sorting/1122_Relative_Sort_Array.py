class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        currentPos = 0
        i=0
        while i < len(arr2):
            for j in range(0,len(arr1)):
                if arr2[i] == arr1[j]:
                    arr1[currentPos], arr1[j] = arr1[j], arr1[currentPos]
                    currentPos += 1
            i = i + 1
        
        x = arr1[currentPos: ]
        x.sort()
        for i in x:
            arr1[currentPos] = i
            currentPos += 1
        return arr1


        
