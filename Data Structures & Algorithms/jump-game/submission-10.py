class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        jump_value = 0
        while index < len(nums) - 1:
           jump_value = nums[index]
           if jump_value == 0:
               return False
           best_index = index
           furthest = index
           for i in range(index + 1, min(index + jump_value + 1, len(nums))):
               if i + nums[i] > furthest:
                   furthest = i + nums[i]
                   best_index = i
           index = best_index
        return True