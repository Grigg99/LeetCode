class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        len_window = 0
        index_flags = []
        swap_counter = 0
        res = 0

        for i in range(len(nums)):
            # print(len_window)

            
            if nums[i] == 0:
                if k == 0:
                    len_window = 0
                    continue

                if swap_counter < k:
                    swap_counter += 1
                    index_flags.append(i)
                    len_window += 1
                
                else:
                    len_window = i - index_flags[0] - 1
                    index_flags.append(i)
                    index_flags.pop(0)
                    len_window += 1
            else:
                len_window += 1

            # print(index_flags)
            
            if res < len_window:
                res = len_window  

        return res
        