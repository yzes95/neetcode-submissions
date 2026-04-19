class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index,number in enumerate(nums):
            #print(index,number)
            if (index+1) < len(nums) and number == nums[index+1]:
                return True
        else:
                return False 