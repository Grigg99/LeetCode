class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k - 1
        sum = 0

        for idx in range(k):
            sum += nums[idx]
        max = sum

        if k == len(nums):
            return sum / k

        while j < len(nums):
            # j += 1
            if j+1 == len(nums):
                break
            sum = sum - nums[i] + nums[j+1]
            # print(sum, i , j)
            if max < sum:
                max = sum
            i += 1
            j += 1


        return max/k