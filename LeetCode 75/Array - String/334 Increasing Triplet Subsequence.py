class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        i = 0
        j = i + 1
        k = len(nums) - 1

        while i < j < k < len(nums):

            if nums[i] < nums[j] < nums[k]:
                return True
            
            if nums[i] >= nums[j]:
                i = j
                j = i + 1

            elif nums[k] < nums[k-1]:
                k = k - 1

            elif nums[j] >= nums[j+1]:
                    j = j + 1
            
            elif nums[k] <= nums[j]:
                k = k - 1

        return False