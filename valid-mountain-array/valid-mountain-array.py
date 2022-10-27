class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxValue = max(arr)
        maxPos = arr.index(maxValue)

        increasing = True
        decreasing = True
        if (len(arr) < 3):
            return False
        if (maxPos==len(arr)-1 or maxPos ==0):
            return False
        for i in range(0, maxPos):
            if (arr[i] >= arr[i+1]):
                increasing = False
        for j in range(maxPos, len(arr)-1):
            print(arr[j], arr[j+1])
            if (arr[j] <= arr[j+1]):
                decreasing = False
        if(increasing==True and decreasing==True):
            return True
        return False