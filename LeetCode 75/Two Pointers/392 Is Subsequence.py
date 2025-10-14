class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        pt = 0
        length = len(t)
        flag = False

        if not s:
            return not flag

        if not t:
            return flag

        for i in range(length):
            if s[ps] == t[i]:
                ps = ps + 1
                if ps == len(s):
                    flag = True
                    break

        return flag