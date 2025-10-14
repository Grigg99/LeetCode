class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.split(" ")
        # print(reversed(new_s))
        # print(new_s)

        res = ""
        for word in reversed(new_s):
            if word:
                res = res + word + " " 
            # print(word, res)

        return res.rstrip()