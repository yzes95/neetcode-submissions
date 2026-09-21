class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sa_sum = nums[0]
        new_sum = nums[0]

        for i in range(1, len(nums)):
            new_sum = max(nums[i], new_sum + nums[i])

            if new_sum > sa_sum:
                sa_sum = new_sum

        return sa_sum


        