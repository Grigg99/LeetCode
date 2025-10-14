class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        prefix_sum = 0
        res = 0

        for i in range(len(gain)):
            prefix_sum += gain[i]
            if res < prefix_sum:
                res = prefix_sum

        return res    