class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        jump_value = 0
        while index < len(nums)-1:
            jump_value = nums[index]

            if jump_value == 0:
                return False

            end_location = index+jump_value
            best_index = index

            for i in range(index + 1,min(end_location+1,len(nums))):
                if (i + nums[i]) > end_location:
                    end_location = i + nums[i]
                    best_index = i
            #print(best_index)

            if end_location >= len(nums) - 1:
                return True

            if best_index == index: 
            #as this means all values ahead will lead to nums[x] = 0, which will trigger the above jump_value == 0 if condition 
                return False
            else:
                index = best_index

        return True