class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1, -1, -1):
            print(i)
            if nums[i] == 0:
                nums.append(nums[i])
                del nums[i]
            
        # print(nums)
        