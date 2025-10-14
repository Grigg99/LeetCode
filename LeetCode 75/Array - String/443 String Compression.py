class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = len(chars) - 1
        calc = 1
        while i > 0:
            if chars[i-1] == chars[i]:
                calc = calc + 1
                del chars[i]
                if i == 1:
                    for idx, item in enumerate(list(str(calc))):
                        chars.insert(i+idx, item)
                    break
            else:
                if calc != 1:
                    for idx, item in enumerate(list(str(calc))):
                        chars.insert(i+1+idx, item)
                calc = 1
            i = i - 1

        print(chars)

        return len(chars)
