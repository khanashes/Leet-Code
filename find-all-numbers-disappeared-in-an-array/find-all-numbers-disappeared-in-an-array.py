class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        obj = Counter(nums).keys()
        result = []

        for i in range(1, len(nums)+1):
            if(i not in obj):
                result.append(i)
        return result