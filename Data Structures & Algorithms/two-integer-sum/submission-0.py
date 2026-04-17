class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
     two_sum_dict = {}
     for i in range(len(nums)):
        complement = target - nums[i]
        if complement in two_sum_dict:
            return [two_sum_dict[complement], i]
        two_sum_dict[nums[i]] = i
        
        
                   


