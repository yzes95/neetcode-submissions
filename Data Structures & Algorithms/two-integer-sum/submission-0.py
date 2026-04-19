class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # temp = nums.copy()
        # if not(2 <= len(nums) <= 1000) or not(-10000000 <= target <= 10000000):
        #     return []
        
        # for index,value in enumerate(nums):
        #     if not(-10000000 <= value <= 10000000):
        #         return []
        #     elif value > target:
        #         temp.pop(index)
        #     for sec_index in range(index+1,len(temp)):
        #         if temp[index] + temp[sec_index] == target:
        #             return [index,sec_index]
        # return []
        seen = {}
        for index,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],index]
            seen[num] = index
        return [] 
