class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u']

        queue = []
        indexes = []
        for idx, char in enumerate(s):
            if char.lower() in vowels:
                queue.append(char)
                indexes.append(idx)
        queue.reverse()

        print(queue)

        char_list = list(s)
        for index, idx in enumerate(indexes):
            char_list[idx] = queue[index]

        return "".join(char_list)
