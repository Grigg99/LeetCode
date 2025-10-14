class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        all_sum = sum(nums)
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if i == 0:
                if all_sum - nums[0] == 0:
                    return 0

            if i != len(nums) - 1:
                if prefix_sum == all_sum - prefix_sum - nums[i+1]:
                    return i+1
            
            if i == len(nums) - 1:
                if prefix_sum - nums[i] == 0:
                    return i
            
        return -1
