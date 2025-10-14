class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        i = 0
        p1 = 0
        p2 = 1
        same_counter = 1
        op_counter = 0
        flags = {}

        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i] == nums[i+1]:
                    same_counter += 1
                else:
                    flags[nums[i]] = same_counter
                    same_counter = 1
            elif same_counter != 1 and nums[-1] == nums[-2]:
                flags[nums[-1]] = same_counter + 1
            else:
                flags[nums[-1]] = 1

        # print(flags)

        for num in list(flags.keys()):
            if k-num in flags:
                if k-num != num:
                    op_counter += min(flags[num], flags[k-num])
                    del flags[num]
                    del flags[k-num]
                else:
                    op_counter += flags[num] // 2
                    del flags[num]

    
            
        return op_counter