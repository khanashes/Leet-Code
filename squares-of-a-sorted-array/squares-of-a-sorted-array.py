class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [x**2 for x in nums]
        squares.sort()
        return squares