class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        

        tmp_len = 0
        zero_i = []
        res = 0
        j = 0

        for i in (range(len(nums))):

            if nums[i] == 0:
                zero_i.append(i)

                # print("G")

                if len(zero_i) > 2:
                    tmp_len = zero_i[-1] - zero_i[j] - 2
                    # print(len(zero_i))
                    j += 1
                    # print(tmp_len)
            
            elif i == len(nums) - 1 and len(zero_i) >= 2:
                # j += 1
                # print(j, zero_i[j])
                tmp_len = len(nums) - zero_i[j] - 2
                # if res < tmp_len:
                #     res = tmp_len
                # j += 1
                # tmp_len = len(nums) - zero_i[j] - 2
                

                    
            if res < tmp_len:
                res = tmp_len
                
        if nums[0] == 1 and len(zero_i) >= 2: 
            if res < zero_i[0]:
                res = zero_i[0]
            if res < zero_i[1] - 1:
                res = zero_i[1] - 1 

        if len(zero_i) == 2 and nums[0]==0 and nums[-1] == 0: 
            return len(nums) - 2
        elif len(zero_i) == 1 or not zero_i:
            return len(nums) - 1

        return res