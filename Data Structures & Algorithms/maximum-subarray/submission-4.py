class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sa_sum = nums[0]
        current_sum = nums[0]

        for i in range(1,len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            sa_sum = max(sa_sum, current_sum)

        return sa_sum


        