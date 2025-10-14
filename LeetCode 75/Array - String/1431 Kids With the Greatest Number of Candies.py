class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        for candy in candies:
            if max < candy: 
                max = candy
        res = []
        for candy in candies:
            res.append(True if candy+extraCandies >= max else False)
        return res