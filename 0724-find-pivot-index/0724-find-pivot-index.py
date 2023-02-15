class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])
        for x in range(len(nums)):
            print(left_sum, right_sum)
            if(left_sum==right_sum):
                return x
            elif x != len(nums)-1:
                left_sum += nums[x]
                right_sum -= nums[x+1]
        return -1