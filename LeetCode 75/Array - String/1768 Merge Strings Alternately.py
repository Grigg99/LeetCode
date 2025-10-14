class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        tmp = ""
        word = word2
        if len(word1) > len(word2):
            word = word1
        for idx, letter in enumerate(word):
            if idx >= len(word1):
                res +=  word2[idx]
            elif idx >= len(word2):
                res += word1[idx]
            else:
                res += word1[idx] + word2[idx]
        return res