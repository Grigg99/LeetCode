class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_consistent_substring(main_string, sub_string):
            if len(sub_string) == 0:
                return False  # A non-empty main_string can't be made of an empty sub_string

            if len(main_string) % len(sub_string) != 0:
                return False  # Main string length must be a multiple of the substring length

            repeat_count = len(main_string) // len(sub_string)

            return sub_string * repeat_count == main_string

        def gcdsofstr(string: str) -> list:
            res = []
            for index, char in enumerate(string):
                if is_consistent_substring(string, string[0 : index + 1]):
                    res.append(string[0 : index + 1])
            return res

        gcds1 = []
        gcds2 = []
        gcds1 = gcdsofstr(str1)
        gcds2 = gcdsofstr(str2)
        print(gcds1, "\n", gcds2)

        l1 = len(gcds1) - 1
        l2 = len(gcds2) - 1

        while l1 >= 0 and l2 >= 0:
            elem1 = gcds1[l1]
            elem2 = gcds2[l2]

            if elem1 == elem2:
                return elem1
            elif len(elem1) > len(elem2):
                l1 -= 1
            else:
                l2 -= 1

        return ""
