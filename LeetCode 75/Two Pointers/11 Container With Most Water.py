class Solution: 
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1
        max = 0
        while i < j:
            area = min(height[i], height[j]) * (j-i)
            if area > max:
                max = area

            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        # print(tmp)
        return max